from models import User
from mongoengine import connect, disconnect

if __name__ == '__main__':
    connect(host='mongodb://mongo-db:27017/users_db')
    user = User(id=1, username='admin')
    user.set_password('secret')
    user.save()
    disconnect('users_db')