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

# 🌟 Custom Styling
custom_theme = gr.themes.Soft(
    primary_hue="amber", 
    secondary_hue="rose", 
    neutral_hue="slate"
)


# 🚀 Gradio Interface
with gr.Blocks(theme=custom_theme) as demo:
    gr.Markdown("## 👩‍🍳 Welcome to **Cheffie** — Your Voice Cooking Assistant!")
    gr.Markdown("Type what you want to cook, choose a language, and Cheffie will guide you!")

    with gr.Row():
        user_input = gr.Textbox(label="🍽️ What would you like to cook?")
        lang_dropdown = gr.Dropdown(choices=["en", "hi", "mr"], value="en", label="🌍 Language")

    output_box = gr.Textbox(label="📋 Recipe Steps", lines=10)

    submit_btn = gr.Button("Let’s Cook! 👨‍🍳")

    submit_btn.click(fn=ask_cheffie, inputs=[user_input, lang_dropdown], outputs=output_box)
    
    gr.Markdown("---")
    gr.Markdown("**Developed by ShravaniJ**")

demo.launch(share=True)
