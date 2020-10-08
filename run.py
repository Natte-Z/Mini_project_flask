import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "randomstring123"
messages = []

def add_message(username, message):
    """without the 0 and 1 the first {} directly refers to the first argument"""
    """add messages to the messages list"""
    now = datetime.now().strptime("%H:%M:%S")
    """ this "({}) {}: {}".format(now, username, message) became message_dict"""
    messages.append({"timestamp": now, "from"_ username, "message": message})

""" because of messages_dict we dont need this anylonger"""
"""def get_all_messages():"""
"""get all of the messages and separate them with a br"""
    """return "<br>".join(messages) """

@app.route('/', methods = ["GET", "POST"])
def index():
    """Main page with instructions"""

    if request.method == "POST":
        session ["username"] = request.form["username"]
        
    if "username" in session:
        return redirect(url_for("user", username=session["username"]))

    return render_template("index.html")

@app.route('/chat/<username>', methods = ["GET", "POST"])
def user(username):
    """add and display chat messages"""

    if request.method == "POST":
        username = session ["username"]
        message = request.form["message"]
        add.message(username, message)
        return redirect(url_for("user", username=session["username"]))

    return render_template("chat.html", username = username, chat_messages = messages)

if __name__ == "__main__":
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)
