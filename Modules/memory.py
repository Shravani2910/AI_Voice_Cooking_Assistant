import json
import os

DATA_FILE = "user_memory.json"

def load_user_data():
    if not os.path.exists(DATA_FILE):
        return {"name": None, "last_recipe": None}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_user_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_user_name():
    data = load_user_data()
    return data.get("name")

def set_user_name(name):
    data = load_user_data()
    data["name"] = name
    save_user_data(data)

def get_last_recipe():
    data = load_user_data()
    return data.get("last_recipe")

def set_last_recipe(recipe):
    data = load_user_data()
    data["last_recipe"] = recipe
    save_user_data(data)

def remember_user(name):
    # Example: Save the name to a file or a variable
    with open("user_memory.json", "w") as f:
        import json
        json.dump({"name": name}, f)

def add_to_history(recipe_title):
    """Add a recipe to the user's cooking history"""
    data = load_user_data()
    if "history" not in data:
        data["history"] = []
    data["history"].append(recipe_title)
    save_user_data(data)


