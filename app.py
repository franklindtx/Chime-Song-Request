import json
from db import db, User, Song
from flask import Flask, request

db_filename = 'chime.db'
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % db_filename
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/')
def default():
    return 'Welcome to the chime song request board!'

@app.route('/users/', methods=['POST'])
def create_user():
    post_body = json.loads(request.data)
    name = post_body.get('name', '')
    user = User(
        name = name
    )
    db.session.add(user)
    db.session.commit()
    return json.dumps({'success': True, 'data': user.serialize()}), 201

@app.route('/users/')
def get_users():
    users = User.query.all()
    res = {'success': True, 'data': [user.serialize() for user in users]}
    return json.dumps(res), 200

@app.route('/user/<int:user_id>/')
def get_user(user_id):
    user = User.query.filter_by(id = user_id).first()
    if not user:
        return json.dumps({'success': False, 'error': 'User not found!'}), 404
    return json.dumps({'success': True, 'data': user.serialize()}), 200

@app.route('/songs/')
def get_songs():
    songs = Song.query.all()
    res = {'success': True, 'data': [song.serialize() for song in songs]}
    return json.dumps(res), 200

@app.route('/user/<string:user_name>/song/', methods = ['POST'])
def create_song(user_name):
    users = User.query.filter_by(name=user_name).first()
    if not users:
        return json.dumps({'success': False, 'error': 'User not found!'}), 404
    post_body = json.loads(request.data)
    song = Song(
        title = post_body.get('title', ''),
        reason = post_body.get('reason', ''),
        detail = post_body.get('detail', ''),
        vote = post_body.get('vote', '')
    )
    users.songs.append(song)
    db.session.add(song)
    db.session.commit()
    return json.dumps({'success': True, 'data': song.serialize()}), 200

@app.route('/song/<int:song_id>/')
def get_song(song_id):
    song = Song.query.filter_by(id = song_id).first()
    if not song:
        return json.dumps({'success': False, 'error': 'Song not found!'}), 404
    return json.dumps({'success': True, 'data': song.serialize()}), 200

@app.route('/song/<int:song_id>/', methods=['DELETE'])
def delete_song(song_id):
    song = Song.query.filter_by(id=song_id).first()
    if not song:
        return json.dumps({'success': False, 'error': 'Song not found!'}), 404
    db.session.delete(song)
    db.session.commit()
    return json.dumps({'success': True, 'data': song.serialize()}), 200

@app.route('/vote/<int:song_id>/', methods=['GET'])
def vote_song(song_id):
    song = Song.query.filter_by(id=song_id).first()
    if not song:
        return json.dumps({'success':False, 'error': 'Song not found!'}), 404
    song.vote += 1
    db.session.commit()
    return json.dumps({'success':True, 'data': song.serialize()}), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
