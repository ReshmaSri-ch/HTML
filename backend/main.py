from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data_handler import load_data, get_city_info

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/cities")
def list_cities():
    data = load_data()
    return list(data.keys())

@app.get("/city/{city_name}")
def get_city(city_name: str):
    data = load_data()
    return get_city_info(data, city_name)