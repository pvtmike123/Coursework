from flask import Flask, render_template
import requests
import json

app = Flask(__name__)
api_key = 'e3b65aa142bd42da8aeb206fcaff4c11'


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


@app.route('/teams')
def team():
    headers = {'X-Auth-Token': api_key, 'X-Response-Control': 'minified'}
    r = requests.get('http://api.football-data.org/v1/competitions/398/teams', headers=headers)
    team_list = r.json()
    print(team_list)
    for team in team_list['teams']:
        print team['crestUrl']
        print team['name']
        print team['squadMarketValue']

    return render_template("teams.html", teams=team_list['teams'])


@app.route('/more-info')
def info():
    headers = {'X-Auth-Token': api_key, 'X-Response-Control': 'minified'}
    r = requests.get('http://api.football-data.org/v1/competitions/398/teams', headers=headers)
    team_list = r.json()
    return render_template("more-info.html", teams=team_list['teams'])


if __name__ == '__main__':
    app.run()
