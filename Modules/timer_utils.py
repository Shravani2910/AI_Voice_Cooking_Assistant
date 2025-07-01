import re
import threading
import time
from modules.voice_output import speak

def extract_minutes(text):
    match = re.search(r"(\d+)\s*(minute|min)", text, re.IGNORECASE)
    return int(match.group(1)) if match else None

def start_timer(minutes):
    def countdown():
        time.sleep(minutes * 60)
        speak(f"{minutes} minutes are up! Step done!")

    thread = threading.Thread(target=countdown)
    thread.daemon = True
    thread.start()
