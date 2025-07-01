import speech_recognition as sr

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("🗣️Human You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        print("❌ Sorry Human, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("❌ STT service error.")
        return ""
