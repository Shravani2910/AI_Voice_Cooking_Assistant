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
