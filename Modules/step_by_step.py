import time
from modules import timer_utils, voice_output

def cook_step_by_step(steps):
    """
    Guides the user through each recipe step via voice.
    """
    for step in steps:
        # Speak the step
        voice_output.speak(f"Step: {step}")
        print(f"🧾 {step}")
        
        # If time-related, extract minutes and start timer
        minutes = timer_utils.extract_minutes(step)
        if minutes:
            voice_output.speak(f"Starting a timer for {minutes} minutes.")
            timer_utils.start_timer(minutes)
        
        # Wait for the user to say "next"
        voice_output.speak("Say 'next' when you're ready to continue.")
        
        while True:
            user_input = input("🗣️ You: ").lower().strip()
            if "next" in user_input:
                break
            elif "stop" in user_input:
                voice_output.speak("Okay, stopping the recipe. Happy cooking!")
                return
            else:
                voice_output.speak("Please say 'next' or 'stop'.")

    voice_output.speak("Recipe complete. Enjoy your meal! 🎉")
