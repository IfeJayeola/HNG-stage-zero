import requests


def get_cat_fact():
    url = "https://catfact.ninja/fact"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['fact']
    except requests.exceptions.HTTPError as errh:
        return("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        return("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        return("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        return("Something went wrong:", err)
