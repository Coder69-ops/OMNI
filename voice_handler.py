
import speech_recognition as sr
import pyttsx3

def listen():
    """
    Listens for voice commands and converts them to text.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            return None

    try:
        command = r.recognize_google(audio)
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        # This is not an error, it just means the audio was not clear enough.
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def speak(text):
    """
    Converts text to speech.
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_feedback(predicted_action):
    """
    Asks the user for feedback on the predicted action.
    """
    speak(f"Was {predicted_action} the correct action?")
    response = listen()
    if response and "yes" in response.lower():
        return True
    return False
