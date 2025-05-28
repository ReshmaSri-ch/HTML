import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.set_page_config(page_title="Tourist Planner", layout="wide")
st.title("🗺️ Tourist Planner")

cities = requests.get(f"{API_URL}/cities").json()
selected_city = st.sidebar.selectbox("Choose a city", cities)

city_info = requests.get(f"{API_URL}/city/{selected_city}").json()

st.header(f"🌆 {selected_city}")
st.markdown(f"**Description:** {city_info.get('description', 'No data')}")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📍 Places to Visit")
    for place in city_info.get("places", []):
        st.markdown(f"- {place}")

with col2:
    st.subheader("🍽️ Foods to Try")
    for food in city_info.get("foods", []):
        st.markdown(f"- {food}")

with col3:
    st.subheader("🏨 Top Restaurants")
    for r in city_info.get("restaurants", []):
        st.markdown(f"- {r}")