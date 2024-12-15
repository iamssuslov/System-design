from flask_mongoengine import MongoEngine
from mongoengine import IntField, StringField
from werkzeug.security import generate_password_hash, check_password_hash

db = MongoEngine()

class User(db.Document):
    id = IntField(primary_key=True)
    username = StringField(unique=True, null=False)
    password_hash = StringField(max_length=512, null=False)

    # Метод для установки пароля
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Метод для проверки пароля
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# Команды
class CreateUserCommand:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password


class UpdateUserPasswordCommand:
    def __init__(self, username, new_password):
        self.username = username
        self.new_password = new_password


# Обработчики команд
class CommandHandler:
    @staticmethod
    def handle_create_user(command: CreateUserCommand):
        user = User(id=command.id, username=command.username)
        user.set_password(command.password)
        user.save()
        return user

    @staticmethod
    def handle_update_user_password(command: UpdateUserPasswordCommand):
        user = User.objects(username=command.username).first()
        if not user:
            raise ValueError("Пользователь не найден")
        user.set_password(command.new_password)
        user.save()
        return user


# Запросы
class GetUserByNameQuery:
    def __init__(self, username):
        self.username = username


# Обработчики запросов
class QueryHandler:
    @staticmethod
    def handle_get_user_by_name(query: GetUserByNameQuery):
        return User.objects(username=query.username).first()

