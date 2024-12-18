from flask import Flask
from flask import request
import requests
# from octokit import Octokit
# from octokit import webhook

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

#getting the details of the user from github 
@app.route("/git", methods = ["POST"])
def git():
    username = request.get_json()['username']

    url = f"https://api.github.com/users/{username}"
    user_data = requests.get(url)
    print(user_data.json())
    return username

#getting the stars count of the user
@app.route("/gitStars", methods = ["POST"])
def gitStar():
    username = request.get_json()['username']
    url = f"https://api.github.com/users/{username}/starred"
    user_data = requests.get(url)
    for i in user_data.json():
        print(i) 
    return {"len": len(user_data.json()), "data":user_data.json()}

#getting the github forks count of the user
@app.route("/gitForks", methods = ["POST"])
def gitForks():
    username = request.get_json()['username']
    url = f"https://api.github.com/users/{username}/repos"
    user_data = requests.get(url)
    forkCount = 0
    for i in user_data.json():
        if i['fork']:
            forkCount += 1
    return {"fork_count":forkCount}
if __name__ == '__main__':
    app.run(debug=True)