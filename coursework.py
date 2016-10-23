from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def generator(file):
    with open(file) as data_file:
        data = json.load(data_file)

    return render_template("teams.html", teams=data['teams'])


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'User'}  # fake user

    return render_template("index.html",
                           title='Home',
                           user=user)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.route('/english_teams')
def team():
    page = generator("/Users/flemin100/Documents/Uni/AWT/coursework/english_teams.json")
    return page


@app.route('/leagues')
def leagues():
    return render_template("leagues.html")


if __name__ == '__main__':
    app.run('0.0.0.0')
