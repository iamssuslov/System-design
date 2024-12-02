from flask_sqlalchemy import SQLAlchemy
import redis
import json
from typing import Type

db = SQLAlchemy()

redis_db = redis.StrictRedis(host='redis', port=6379, decode_responses=True)


class Folder(db.Model):
    __tablename__ = 'folders'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('folders.id'), nullable=True)
    owner_id = db.Column(db.Integer, nullable=False)

    parent = db.relationship('Folder', remote_side=[id], backref='subfolders')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "parent_id": self.parent_id,
            "owner_id": self.owner_id,
            "parent": self.parent
        }

    @staticmethod
    def from_dict(data):
        folder = Folder()
        folder.id = data.get("id")
        folder.name = data.get("name")
        folder.parent_id = data.get("parent_id")
        folder.owner_id = data.get("owner_id")
        folder.parent = data.get("parent_id")
        return folder


class File(db.Model):
    __tablename__ = 'files'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    folder_id = db.Column(db.Integer, db.ForeignKey('folders.id'), nullable=False)
    owner_id = db.Column(db.Integer, nullable=False)
    content = db.Column(db.LargeBinary, nullable=True)

    folder = db.relationship('Folder', backref='files')

    def to_dict(self):
        return {
            "id": self.id,
            "filename": self.filename,
            "folder_id": self.folder_id,
            "owner_id": self.owner_id,
            "content": self.content.decode("utf-8"),
        }

    @staticmethod
    def from_dict(data):
        folder = Folder()
        folder.id = data.get("id")
        folder.filename = data.get("filename")
        folder.folder_id = data.get("folder_id")
        folder.owner_id = data.get("owner_id")
        folder.content = data.get("content")
        return folder


def get_from_cache_or_db(cache_key, query_func, table: Type[Folder] | Type[File], expire_time=60):
    cached_data = redis_db.get(cache_key)
    if cached_data:
        object_instance = table.from_dict(json.loads(cached_data))
        return table.query.filter_by(id=object_instance.id, owner_id=object_instance.owner_id).first()

    data = query_func()

    redis_db.setex(cache_key, expire_time, json.dumps(data.to_dict()))
    return data
