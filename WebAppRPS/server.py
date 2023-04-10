from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Dictionary to keep track of active game rooms
active_rooms = {}

# Index route
@app.route('/')
def index():
    return render_template('index.html')

# Event handler for "join" event
@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)

    if room not in active_rooms:
        active_rooms[room] = []

    active_rooms[room].append(username)

    if len(active_rooms[room]) == 2:
        # Start the game
        emit('start_game', {'users': active_rooms[room]}, room=room)

# Event handler for "play" event
@socketio.on('play')
def on_play(data):
    username = data['username']
    room = data['room']
    choice = data['choice']
    opponent_choice = None

    for user in active_rooms[room]:
        if user != username:
            opponent_choice = user_choice[room]
            break

    emit('result', {'choice': choice, 'opponent_choice': opponent_choice}, room=room)

# Event handler for "leave" event
@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)

    if room in active_rooms:
        active_rooms[room].remove(username)

        if len(active_rooms[room]) == 0:
            del active_rooms[room]

# Start the app
if __name__ == '__main__':
    socketio.run(app, debug=True)
