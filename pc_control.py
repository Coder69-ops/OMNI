import webbrowser
import os
import subprocess
import datetime

def open_browser():
    """
    Opens the default web browser.
    """
    webbrowser.open("https://www.google.com")

def search_web(query, engine="google"):
    """
    Searches the web with the given query on the specified search engine.
    """
    engine = engine.lower()
    if engine == "duckduckgo":
        webbrowser.open(f"https://duckduckgo.com/?q={query}")
    elif engine == "bing":
        webbrowser.open(f"https://www.bing.com/search?q={query}")
    else:
        webbrowser.open(f"https://www.google.com/search?q={query}")

def take_screenshot(filename=None):
    """
    Takes a screenshot and saves it to the desktop.
    If no filename is provided, it saves with a timestamp.
    """
    import pyautogui
    screenshot = pyautogui.screenshot()
    desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    
    if filename:
        if not filename.lower().endswith('.png'):
            filename += '.png'
    else:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"screenshot_{timestamp}.png"
        
    screenshot_path = os.path.join(desktop_path, filename)
    screenshot.save(screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")

def run_terminal_command(command):
    """
    Executes a terminal command and prints the output in real-time.
    """
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Real-time output
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output.strip())
        
        # Capture any remaining error output
        stderr = process.communicate()[1]
        if stderr:
            print("Error output:")
            print(stderr.strip())

    except Exception as e:
        print(f"Error executing command: {command}")
        print(e)
