import requests

def get_geopolitical_sentiment():
    url = "https://api.gdeltproject.org/api/v2/doc/doc?query=conflict OR war OR escalation&mode=artlist&format=json"
    try:
        response = requests.get(url)
        return response.json().get("articles", [])
    except Exception:
        return []