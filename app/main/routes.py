# Import necessary modules from Flask and requests
from flask import render_template, request, jsonify
from . import main
import requests

# Define the route for the index page, handling both GET and POST requests
@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the GitHub username from the form submission
        username = request.form.get('username')
        # Fetch GitHub statistics for the given username
        stats = get_github_stats(username)
        # Render the index.html template with the username and stats
        return render_template('index.html', username=username, stats=stats)
    # Render the index.html template for GET requests
    return render_template('index.html')

# Function to fetch GitHub statistics for a given username
def get_github_stats(username):
    url = "https://api.github.com/users/{}".format(username)
    # Send a GET request to the GitHub API
    response = requests.get(url)
    if response.status_code == 200:
        # If the request is successful, parse the JSON response
        data = response.json()
        # Extract relevant stats from the response data
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
        # If the request fails, return an error message
        return {"error": "User not found or API rate limit exceeded"}
