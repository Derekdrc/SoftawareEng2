from flask import Flask, render_template, request
import threading
import time

app = Flask(__name__)

# initialize players as None
player1 = None
player2 = None

# dictionary to store player choices
player_choices = {}

# dictionary to store the result of the game
game_results = {}


def play_game():
    global player1, player2, player_choices, game_results

    # wait until both players have made their choices
    while player_choices.get(player1) is None or player_choices.get(player2) is None:
        time.sleep(1)

    # get the choices made by each player
    player1_choice = player_choices.get(player1)
    player2_choice = player_choices.get(player2)

    # determine the result of the game
    if player1_choice == player2_choice:
        result = "It's a tie!"
    elif player1_choice == 'rock':
        if player2_choice == 'paper':
            result = "Player 2 wins!"
        else:
            result = "Player 1 wins!"
    elif player1_choice == 'paper':
        if player2_choice == 'scissors':
            result = "Player 2 wins!"
        else:
            result = "Player 1 wins!"
    else: # player1_choice == 'scissors'
        if player2_choice == 'rock':
            result = "Player 2 wins!"
        else:
            result = "Player 1 wins!"

    # store the result of the game
    game_results[player1] = result
    game_results[player2] = result


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/play', methods=['GET', 'POST'])
def play():
    global player1, player2, player_choices, game_results

    # if no player has joined, assign them to player1
    if player1 is None:
        player1 = request.sid
        return render_template('waiting.html', player=1)

    # if player1 has joined but not player2, assign them to player2
    elif player2 is None:
        player2 = request.sid
        return render_template('waiting.html', player=2)

    # if both players have joined, play the game
    else:
        # assign current player's choice
        player_choices[request.sid] = request.form['choice']

        # start game in a separate thread
        threading.Thread(target=play_game).start()

        # wait for game to finish
        time.sleep(1)

        # display the result of the game to both players
        result = game_results.get(request.sid)
        return render_template('result.html', player1_choice=player_choices.get(player1), 
                               player2_choice=player_choices.get(player2), result=result)


if __name__ == '__main__':
    app.run(debug=True)
