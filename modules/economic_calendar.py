import requests

def get_economic_events():
    url = "https://api.tradingeconomics.com/calendar/country/all"
    key = "aecf32867c24474:ppm7k7m4hh8i140"
    try:
        response = requests.get(f"{url}?c={key}")
        return response.json()
    except Exception:
        return []