import aiohttp
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv('API_KEY')

class WeatherInfo(BaseModel):
    name: str
    weather: str
    temp: float
    feels_like: float
    wind_speed: float


async def get_weather(city: str) -> WeatherInfo | None:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            return WeatherInfo(
                name=data['name'],
                weather=data['weather'][0]['description'],
                temp=data['main']['temp'],
                feels_like=data['main']['feels_like'],
                wind_speed=data['wind']['speed']
            ) if data['cod'] == 200 else None

