from models import db
from app import app

if __name__ == '__main__':
    with app.app_context():
        db.create_all()