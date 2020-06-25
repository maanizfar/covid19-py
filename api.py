import requests
import json

summary_url = 'https://api.covid19api.com/summary'


def get_summary():
    try:
        res = requests.get(summary_url)
        res.raise_for_status()

        if res.ok:
            return json.loads(res.text)

    except Exception as err:
        print(f"An error occured: {err}")
