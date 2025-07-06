import requests

API_KEY = "140d08423c7844aeac70244c3b7f7443"
BASE_URL = "https://api.spoonacular.com/recipes/complexSearch"

def find_recipe(query, number=1):
    params = {
        "query": query,
        "number": 1,
        "addRecipeInformation": True,
        "instructionsRequired": True,
        "apiKey": API_KEY
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        if data["results"]:
            return data["results"]
        else:
            return []
    else:
        print(f"Recipe Not Found!: {response.status_code}")
        return []

def get_recipe_steps(recipe_id):
    info_url = f"https://api.spoonacular.com/recipes/{recipe_id}/analyzedInstructions"
    params = {
        "apiKey": API_KEY
    }

    response = requests.get(info_url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data and len(data) > 0 and "steps" in data[0]:
            return data[0]["steps"]
        else:
            return []
    else:
        print(f"API Error: {response.status_code}")
        return []

def search_recipe(query):
    """Search for a recipe and return title and steps"""
    recipes = find_recipe(query)
    if recipes:
        recipe = recipes[0]
        recipe_id = recipe["id"]
        steps = get_recipe_steps(recipe_id)
        
        # Extract step text from the steps
        step_texts = []
        for step in steps:
            if isinstance(step, dict) and "step" in step:
                step_texts.append(step["step"])
            else:
                step_texts.append(str(step))
        
        return recipe["title"], step_texts
    else:
        return None, []
    
