from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Folder(db.Model):
    __tablename__ = 'folders'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('folders.id'), nullable=True)
    owner_id = db.Column(db.Integer, nullable=False)

    parent = db.relationship('Folder', remote_side=[id], backref='subfolders')

class File(db.Model):
    __tablename__ = 'files'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    folder_id = db.Column(db.Integer, db.ForeignKey('folders.id'), nullable=False)
    owner_id = db.Column(db.Integer, nullable=False)
    content = db.Column(db.LargeBinary, nullable=True)

    folder = db.relationship('Folder', backref='files')
