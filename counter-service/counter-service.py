#!flask/bin/python
from flask import Flask, request
import os
import json

app = Flask(__name__)
COUNTER_FILE = "counter.json"


# Load counter from file
def load_counter():
    if os.path.exists(COUNTER_FILE):
        try:
            with open(COUNTER_FILE, "r") as f:
                data = json.load(f)
                return data.get("counter", 0)
        except Exception:
            return 0
    return 0


# Save counter to file
def save_counter(value):
    with open(COUNTER_FILE, "w") as f:
        json.dump({"counter": value}, f)


counter = load_counter()


@app.route('/', methods=["POST", "GET"])
def index():
    global counter
    if request.method == "POST":
        counter += 1
        save_counter(counter)
        return "Hmm, Plus 1 please\n"
    else:
        return f"Our counter is: {counter}\n"


if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
