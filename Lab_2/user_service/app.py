from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token
from config import Config
from models import db, GetUserByNameQuery, QueryHandler, CreateUserCommand, CommandHandler

app = Flask(__name__)
app.config.from_object(Config)
app.config['JSON_AS_ASCII'] = False

db.init_app(app)
jwt = JWTManager(app)

id = 5 # знаю, что это не самое лучшее решение, но для упрощения установки id для пользователей подойдёт


@app.route('/register', methods=['POST'])
def register():
    global id
    data = request.get_json()

    get_user_query = GetUserByNameQuery(username=data['username'])
    user = QueryHandler.handle_get_user_by_name(get_user_query)

    if user:
        return jsonify({'message': 'Пользователь уже существует'}), 400

    create_user_command = CreateUserCommand(id=id, username=data['username'], password=data['password'])
    CommandHandler.handle_create_user(create_user_command)
    id += 1

    return jsonify({'message': 'Пользователь успешно зарегистрирован'}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    get_user_query = GetUserByNameQuery(username=data['username'])
    user = QueryHandler.handle_get_user_by_name(get_user_query)

    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=str(user.id))
        return jsonify({'access_token': access_token}), 200

    return jsonify({'message': 'Неверные учетные данные'}), 401


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
