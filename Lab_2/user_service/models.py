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
