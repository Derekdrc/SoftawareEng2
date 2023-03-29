from flask import Flask, request, render_template

def flask_thread():
    #Create flask webhost
    app = Flask(__name__)

    #flask --app main run (--host 0.0.0.0) to host, with optional outside exposure
    
    @app.route("/")
    def flask_rps(name=None):
        return render_template('flaskhtml.html', name=name)

    @app.route("/test" , methods=['GET', 'POST'])
    def test():
        select = request.form.get('rps-list-choices')
        print(select)
        return(str(select)) # just to see what select is
    
    app.run()

if __name__ == '__main__':
    flask_thread()