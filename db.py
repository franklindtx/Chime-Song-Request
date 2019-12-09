from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

song_table = db.Table('songTable', db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('song_id', db.Integer, db.ForeignKey('song.id'))
)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    songs = db.relationship('Song', secondary = song_table, back_populates = 'users')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.songs = []

    def serialize(self):
        return {
            'id':self.id,
            'name': self.name,
            'songs': [s.serialize() for s in self.songs]
        }

class Song(db.Model):
    __tablename__ = 'song'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)
    reason = db.Column(db.String, nullable = False)
    detail = db.Column(db.String, nullable = False)
    vote = db.Column(db.Integer, nullable = False)
    users = db.relationship('User', secondary = song_table, back_populates = 'songs')

    def __init__(self, **kwargs):
        self.title = kwargs.get('title', '')
        self.reason = kwargs.get('reason', '')
        self.detail = kwargs.get('detail', '')
        self.vote = 0

    def serialize(self):
        return {
            'id':self.id,
            'title':self.title,
            'reason':self.reason,
            'detail':self.detail,
            'vote':self.vote
        }
