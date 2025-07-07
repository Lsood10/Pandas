
import json

def save_history(history, filename="chat_history.json"):
    with open(filename, "w") as f:
        json.dump(history, f, indent=4)

def load_history(filename="chat_history.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []