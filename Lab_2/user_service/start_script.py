from models import db, User
from app import app

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if not User.query.filter_by(username='admin').first():
            admin = User(username='admin')
            admin.set_password('secret')
            db.session.add(admin)
            db.session.commit()