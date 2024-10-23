from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token
from config import Config
from models import db, User

app = Flask(__name__)
app.config.from_object(Config)
app.config['JSON_AS_ASCII'] = False

db.init_app(app)
jwt = JWTManager(app)

# Создание таблиц и администратора перед первым запросом
@app.before_first_request
def create_tables():
    db.create_all()
    if not User.query.filter_by(username='admin').first():
        admin = User(username='admin')
        admin.set_password('secret')
        db.session.add(admin)
        db.session.commit()

# Эндпоинт для регистрации пользователя
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Пользователь уже существует'}), 400

    user = User(username=data['username'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'Пользователь успешно зарегистрирован'}), 201

# Эндпоинт для авторизации пользователя
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    user = User.query.filter_by(username=data['username']).first()

    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify({'access_token': access_token}), 200

    return jsonify({'message': 'Неверные учетные данные'}), 401

if __name__ == '__main__':
    app.run(port=5000, debug=True)
