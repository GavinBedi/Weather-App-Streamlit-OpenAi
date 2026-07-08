
import requests
import streamlit as st

from openai import OpenAI

import os
from dotenv import load_dotenv

loaded = load_dotenv()
print("Dotenv loaded:", loaded)
print("Current directory:", os.getcwd())

openai_api_key = os.getenv("OPENAI_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

print("OpenAI:", openai_api_key)
print("Weather:", WEATHER_API_KEY)




def get_weather(city):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={WEATHER_API_KEY}"
    )

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return None






def generate_weather_description(weather_data, openai_api_key):

    client = OpenAI(api_key=openai_api_key)

    description = weather_data["weather"][0]["description"]
    temp = weather_data["main"]["temp"] - 273.15
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]

    prompt = f"""
    The weather in {weather_data['name']} is:

    Description: {description}
    Temperature: {temp:.2f} °C
    Humidity: {humidity}%
    Wind Speed: {wind_speed} m/s

    Give a friendly weather summary in about 60 words.
    """

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    return response.output_text
def main():

    st.set_page_config(
        page_title="AI Weather App",
        page_icon="🌦️",
        layout="wide",
    )

    st.title("🌦️ AI Weather Assistant")

    city = st.sidebar.text_input(
        "Enter City",
        "London",
    )

    if st.sidebar.button("Get Weather"):

        with st.spinner("Fetching weather..."):

            weather = get_weather(city)

        if weather is None:

            st.error("City not found!")

            return

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "🌡 Temperature",
                f"{weather['main']['temp']-273.15:.1f} °C",
            )

            st.metric(
                "💧 Humidity",
                f"{weather['main']['humidity']} %",
            )

        with col2:

            st.metric(
                "🌬 Wind Speed",
                f"{weather['wind']['speed']} m/s",
            )

            st.metric(
                "☁ Weather",
                weather["weather"][0]["description"].title(),
            )

        st.divider()

        st.subheader("🤖 AI Weather Summary")

        with st.spinner("Thinking..."):

            summary = generate_weather_description(
    weather,
    openai_api_key
)
        st.success(summary)


if __name__ == "__main__":
    main()