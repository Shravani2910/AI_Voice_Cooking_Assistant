from modules.voice_input import listen_command
from modules import recipe_search
from modules import step_by_step
from modules import memory
from modules import voice_output

lang_choice = input("Choose language (en/hi/mr): ").strip().lower()

# Multilingual greeting
if lang_choice == "hi":
    voice_output.speak("नमस्ते! आज आप क्या बनाना चाहते हैं?", lang='hi')
elif lang_choice == "mr":
    voice_output.speak("नमस्कार! काय बनवायचं आहे?", lang='mr')
else:
    voice_output.speak("Hello! What would you like to cook today?", lang='en') 

# Get or ask for user name
name = memory.get_user_name()
if not name: 
    voice_output.speak("Hello! What's your name?")
    name = listen_command()
    memory.remember_user(name)

voice_output.speak(f"Hi {name}, I'm Cheffie. What would you like to cook today?")
query = listen_command()

# Search and cook
recipe = recipe_search.find_recipe(query)
if recipe:
    recipe_title = recipe[0]["title"] if isinstance(recipe, list) and recipe else recipe["title"]
    memory.add_to_history(recipe_title)
    voice_output.speak(f"I found a recipe: {recipe_title}. Let's begin!")
    recipe_id = recipe[0]["id"] if isinstance(recipe, list) and recipe else recipe["id"]
    steps = recipe_search.get_recipe_steps(recipe_id)
    if steps:
        
        step_texts = [s["step"] if isinstance(s, dict) and "step" in s else str(s) for s in steps]
        step_by_step.cook_step_by_step(step_texts)
    else:
        voice_output.speak("Sorry, I couldn't find step-by-step instructions for this recipe.")
else:
    voice_output.speak("Sorry, I couldn't find any recipe matching your request.")
