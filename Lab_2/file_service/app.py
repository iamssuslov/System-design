from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from config import Config
from models import db, Folder, File

app = Flask(__name__)
app.config.from_object(Config)
app.config['JSON_AS_ASCII'] = False

db.init_app(app)
jwt = JWTManager(app)

# Создание таблиц перед первым запросом
@app.before_first_request
def create_tables():
    db.create_all()

# Эндпоинт для создания папки
@app.route('/folders', methods=['POST'])
@jwt_required()
def create_folder():
    data = request.get_json()
    user_id = get_jwt_identity()

    folder = Folder(
        name=data['name'],
        parent_id=data.get('parent_id'),
        owner_id=user_id
    )
    db.session.add(folder)
    db.session.commit()

    return jsonify({'message': 'Папка успешно создана', 'folder_id': folder.id}), 201

# Эндпоинт для получения содержимого папки
@app.route('/folders/<int:folder_id>', methods=['GET'])
@jwt_required()
def get_folder_contents(folder_id):
    user_id = get_jwt_identity()
    folder = Folder.query.filter_by(id=folder_id, owner_id=user_id).first()

    if not folder:
        return jsonify({'message': 'Папка не найдена'}), 404

    subfolders = [
        {'id': f.id, 'name': f.name}
        for f in folder.subfolders if f.owner_id == user_id
    ]
    files = [
        {'id': f.id, 'filename': f.filename}
        for f in folder.files if f.owner_id == user_id
    ]

    return jsonify({'subfolders': subfolders, 'files': files}), 200

# Эндпоинт для загрузки файла

@app.route('/files', methods=['POST'])
@jwt_required()
def upload_file():
    user_id = get_jwt_identity()

    if 'file' not in request.files:
        return jsonify({'message': 'Нет файла в запросе'}), 400

    file = request.files['file']
    folder_id = request.form.get('folder_id')

    if not folder_id:
        return jsonify({'message': 'Не указан folder_id'}), 400

    folder = Folder.query.filter_by(id=folder_id, owner_id=user_id).first()
    if not folder:
        return jsonify({'message': 'Папка не найдена'}), 404

    new_file = File(
        filename=file.filename,
        content=file.read(),
        folder_id=folder_id,
        owner_id=user_id
    )
    db.session.add(new_file)
    db.session.commit()

    return jsonify({'message': 'Файл успешно загружен', 'file_id': new_file.id}), 201

# Эндпоинт для скачивания файла
@app.route('/files/<int:file_id>', methods=['GET'])
@jwt_required()
def download_file(file_id):
    user_id = get_jwt_identity()
    file = File.query.filter_by(id=file_id, owner_id=user_id).first()

    if not file:
        return jsonify({'message': 'Файл не найден'}), 404

    response = make_response(file.content)
    response.headers.set('Content-Type', 'application/octet-stream')
    response.headers.set('Content-Disposition', 'attachment', filename=file.filename)
    return response

if __name__ == '__main__':
    app.run(port=5001, debug=True)
