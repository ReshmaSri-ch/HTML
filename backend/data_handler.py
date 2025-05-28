import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "cities.json")

def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def get_city_info(data, city):
    return data.get(city, {})