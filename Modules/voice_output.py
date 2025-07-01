import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print(f"Cheffie: {text}")
    engine.say(text)
    engine.runAndWait()