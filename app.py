import gradio as gr
from modules import voice_output, recipe_search, step_by_step, memory

# Default language
lang = "en"

def ask_cheffie(user_input, lang_choice):
    global lang
    lang = lang_choice
    user_name = memory.get_user_name() or "Chef"
    voice_output.speak(f"{user_name}, searching for your recipe...", lang)

    recipe_title, steps = recipe_search.search_recipe(user_input)

    if recipe_title and steps:
        memory.set_last_recipe(recipe_title)
        voice_output.speak(f"I found {recipe_title}. Let’s begin!", lang)
        steps_text = "\n".join([f"Step {i+1}: {step}" for i, step in enumerate(steps)])
        return f"{recipe_title}\n\n{steps_text}"
    else:
        voice_output.speak("Sorry, I couldn't find any recipe.", lang)
        return "Recipe not found."

iface = gr.Interface(
    fn=ask_cheffie,
    inputs=[
        gr.Textbox(label="What would you like to cook?"),
        gr.Dropdown(choices=["en", "hi", "mr"], value="en", label="Choose Language")
    ],
    outputs="text",
    title="👩‍🍳 Cheffie – Your Voice Cooking Assistant",
    description="Type your dish. Cheffie will find the recipe and speak in your chosen language!"
)

iface.launch()
