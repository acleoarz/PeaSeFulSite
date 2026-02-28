from flask import Flask, render_template
from flask_socketio import SocketIO, send
import os
import secrets

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") or secrets.token_hex(32)

socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def home():
    return render_template("index.html")

@socketio.on("message")
def handle_message(data):
    send(data, broadcast=True)

if __name__ == "__main__":
    socketio.run(
        app,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
