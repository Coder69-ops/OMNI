import json
import os

def start_session():
    """
    Starts a new session.
    """
    if not os.path.exists("session_logs"): 
        os.makedirs("session_logs")

def log_interaction(interaction, action):
    """
    Logs a user interaction to a file.
    """
    with open("session_logs/interactions.jsonl", "a") as f:
        f.write(json.dumps({"interaction": interaction, "action": action}) + "\n")

def get_session_context():
    """
    Retrieves the current session context.
    """
    # In a real application, this would be more sophisticated.
    # For now, we'll just read the last interaction.
    if not os.path.exists("session_logs/interactions.jsonl"): return None
    with open("session_logs/interactions.jsonl", "r") as f:
        lines = f.readlines()
        if not lines: return None
        last_interaction = json.loads(lines[-1])
        return last_interaction
