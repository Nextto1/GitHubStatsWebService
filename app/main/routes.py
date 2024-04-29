from flask import render_template, request, jsonify
from . import main
import requests

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
       stats = get_github_stats(username)
        return render_template('index.html', username=username, stats=stats)
    return render_template('index.html')

def get_github_stats(username):
    url = "https://api.github.com/users/{}".format(username)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        stats = {
            'username': username,
            'profile_image': data.get('avatar_url'),
            'num_repos': data.get('public_repos'),
            'followers': data.get('followers'),
            'following': data.get('following'),
            'public_gists': data.get('public_gists'),
            'bio': data.get('bio'),
        }
        return stats
    else:
        return {"error": "User not found or API rate limit exceeded"}
