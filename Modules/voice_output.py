from gtts import gTTS
import os
import pygame
import tempfile


def speak(text, lang='en'):
    try:
        print(f"🤖 Cheffie Speaking ({lang}): {text}")
        tts = gTTS(text=text, lang=lang)
        # Create temporary file without auto-delete to avoid permission issues
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        temp_file.close()
        tts.save(temp_file.name)
        
        # Initialize pygame mixer for audio playback
        pygame.mixer.init()
        pygame.mixer.music.load(temp_file.name)
        pygame.mixer.music.play()
        
        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.wait(100)
        
        # Add a small delay to ensure file is not in use
        pygame.time.wait(500)
        
        # Clean up after playing
        try:
            os.unlink(temp_file.name)
        except OSError:
            # If file is still in use, just leave it - it will be cleaned up later
            pass
    except Exception as e:
        print(f"⚠️ Error speaking: {e}")

