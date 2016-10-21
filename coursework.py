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


@app.route('/more-info')
def info():
    headers = {'X-Auth-Token': api_key, 'X-Response-Control': 'minified'}
    r = requests.get('http://api.football-data.org/v1/competitions/398/teams', headers=headers)
    team_list = r.json()
    return render_template("more-info.html", teams=team_list['teams'])


if __name__ == '__main__':
    app.run('0.0.0.0')
