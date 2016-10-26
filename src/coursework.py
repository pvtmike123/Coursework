from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

# generator function loads .json file which then renders on teams.html

def generator(file):
    with open(file) as data_file:
        data = json.load(data_file)

    return render_template("teams.html", teams=data['teams'])


def api(file):
    with open(file) as data_file:
        data = json.load(data_file)

    return render_template("api.html", teams=data['teams'])


def country(file):
    with open(file) as data_file:
        data = json.load(data_file)

    return render_template("leagues.html", teams=data['teams'])


@app.route('/')
@app.route('/index')
def index():

    return render_template("index.html",
                           title='Home')


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.route('/english_teams')
def team():
    page = generator("/home/tc/Coursework/Coursework/english_teams.json")
    return page


@app.route('/scottish_teams')
def team_1():
    page = generator("/home/tc/Coursework/Coursework/scottish_teams.json")
    return page


@app.route('/germany_teams')
def team_2():
    page = generator("/home/tc/Coursework/Coursework/germany_teams.json")
    return page


@app.route('/leagues')
def leagues():
    page = country("/home/tc/Coursework/Coursework/coursework/leagues.json")
    return page


@app.route('/api')
def api():
    page = api("/home/tc/Coursework/Coursework/english_teams.json")
    return page


@app.route('/info')
def moreinfo():

    return render_template("more-info.html")


if __name__ == '__main__':
    app.run('0.0.0.0')
