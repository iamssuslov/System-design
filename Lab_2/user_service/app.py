from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token
from config import Config
from models import db, User

app = Flask(__name__)
app.config.from_object(Config)
app.config['JSON_AS_ASCII'] = False

db.init_app(app)
jwt = JWTManager(app)


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if User.objects(username=data['username']).first():
        return jsonify({'message': 'Пользователь уже существует'}), 400

    user = User(username=data['username'])
    user.set_password(data['password'])
    user.save()

    return jsonify({'message': 'Пользователь успешно зарегистрирован'}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    user = User.objects(username=data['username']).first()

    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify({'access_token': access_token}), 200

    return jsonify({'message': 'Неверные учетные данные'}), 401


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
