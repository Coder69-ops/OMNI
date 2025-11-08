
import pc_control
import api_integrations

def route_command(command, action):
    """
    Routes the user's command to the appropriate module based on the predicted action.
    """
    if action == "open_browser":
        pc_control.open_browser()
    elif action == "search_web":
        # Extract the search query and engine from the command
        parts = command.split("search for ")[-1].strip()
        query = parts
        engine = "google"
        if " on " in parts:
            query, engine = parts.split(" on ")
        pc_control.search_web(query, engine)
    elif action == "take_screenshot":
        filename = None
        if " as " in command:
            filename = command.split(" as ")[-1].strip()
        pc_control.take_screenshot(filename=filename)
    elif action == "make_call":
        # Extract the phone number from the command
        to_number = command.split("to ")[-1].strip()
        api_integrations.make_call(to_number)
    elif action == "run_terminal_command":
        # Extracts the terminal command from the user's speech
        terminal_command = command.split("run the terminal command")[-1].strip()
        pc_control.run_terminal_command(terminal_command)
    else:
        # Default action or command not recognized
        print(f"Executing default action for command: {command}")

