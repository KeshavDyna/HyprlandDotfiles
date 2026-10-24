#!/usr/bin/env python3

import json
import urllib.request

# Change these coordinates to your city.
LATITUDE = 30.692001
LONGITUDE = 76.846797
CITY = "Panchkula"

WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Rime fog",
    51: "Light drizzle",
    53: "Drizzle",
    55: "Heavy drizzle",
    61: "Light rain",
    63: "Rain",
    65: "Heavy rain",
    71: "Light snow",
    73: "Snow",
    75: "Heavy snow",
    80: "Rain showers",
    81: "Heavy showers",
    82: "Violent showers",
    95: "Thunderstorm",
    96: "Thunderstorm with hail",
    99: "Heavy thunderstorm",
}

WEATHER_ICONS = {
    0: ("☀️", "🌙"),
    1: ("🌤️", "🌙☁️"),
    2: ("⛅", "🌙☁️"),
    3: ("☁️", "☁️"),
    45: ("🌫", "🌫"),
    48: ("🌫", "🌫"),
    51: ("🌦️", "🌧️"),
    53: ("🌧️", "🌧️"),
    55: ("🌧️", "🌧️"),
    56: ("🌧️", "🌧️"),
    57: ("🌧️", "🌧️"),
    61: ("🌦️", "🌧️"),
    63: ("🌧️", "🌧️"),
    65: ("🌧️", "🌧️"),
    66: ("🌧️", "🌧️"),
    67: ("🌧️", "🌧️"),
    71: ("🌨️", "🌨️"),
    73: ("❄️", "❄️"),
    75: ("❄️", "❄️"),
    77: ("❄️", "❄️"),
    80: ("🌦️", "🌧️"),
    81: ("🌧️", "🌧️"),
    82: ("⛈️", "⛈️"),
    85: ("🌨️", "🌨️"),
    86: ("❄️", "❄️"),
    95: ("⛈️", "⛈️"),
    96: ("⛈️", "⛈️"),
    99: ("⛈️", "⛈️"),
}

def main():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={LATITUDE}&longitude={LONGITUDE}"
        "&current=temperature_2m,relative_humidity_2m,"
        "apparent_temperature,weather_code,wind_speed_10m"
        "&timezone=auto""&current=temperature_2m,relative_humidity_2m,"
        "apparent_temperature,weather_code,wind_speed_10m,is_day"
    )

    request = urllib.request.Request(
        url,
        headers={"User-Agent": "WaybarWeather/1.0"}
    )

    with urllib.request.urlopen(request, timeout=8) as response:
        data = json.loads(response.read().decode())

    current = data["current"]
    temperature = round(current["temperature_2m"])
    feels_like = round(current["apparent_temperature"])
    humidity = current["relative_humidity_2m"]
    wind = current["wind_speed_10m"]
    code = current["weather_code"]

    condition = WEATHER_CODES.get(code, "Weather unavailable")

    is_day = current["is_day"] == 1
    day_icon, night_icon = WEATHER_ICONS.get(
    code, ("🌡", "🌡")
    )
    icon = day_icon if is_day else night_icon

    output = {
        "text": (
            f'<span size="13000">{icon}</span> '
            f"{condition} {temperature}°C"
        ),
        "tooltip": (
            f"{CITY} · {condition}\n"
            f"Temperature: {temperature}°C\n"
            f"Feels like: {feels_like}°C\n"
            f"Humidity: {humidity}%\n"
            f"Wind: {wind} km/h"
        ),
        "class": "weather",
    }


    print(json.dumps(output, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print(json.dumps({
            "text": "󰖐 --",
            "tooltip": "Weather unavailable. Check your internet connection.",
            "class": "weather-unavailable",
        }, ensure_ascii=False))
