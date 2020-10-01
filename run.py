import os
from flask import Flask, redirect

app = Flask(__name__)
messages = []

def add_messages(username, message):
    """without the 0 and 1 the first {} directly refers to the first argument"""
    """add messages to the messages lst"""
    messages.append("{}: {}".format(username, message))

def get_all_messages():
"""get all of the messages and separate them with a br"""
    return "<br>".join(messages)

@app.route('/')
def index():
    """Main page with instructions"""
    return "TO send a message use /USERNAME/MESSAGE"

@app.route('/<username>')
def user(username):
    """Display chat messages"""
    return "<h1>Welcome, {0}</h1>{1}".format (username, get_all_message())

@app.route('/<username/<message>')
    def send_message(username, message):
        """Create new messages and redirect back to the chat page"""
        add_messages(username, message)
        return redirect("/" + username)

if __name__ == "__main__":
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)
