from flask import Flask, request, render_template
import time
import multiprocessing

choice = 0
app = Flask(__name__)
app.config['choice'] = multiprocessing.Value('i', 0)
#flask --app main run (--host 0.0.0.0) to host, with optional outside exposure

@app.route("/", methods=['GET', 'POST'])
def flask_rps():
    if request.method == 'POST':
        choice = request.form.get('rps-list-choices', -1)
        app.config['choice'].value = int(choice)

    return render_template('flaskhtml.html')

def value_updater():
    global choice
    while True:
        choice = app.config['choice']
        time.sleep(1)


def run():
    app.run(use_reloader=False)
