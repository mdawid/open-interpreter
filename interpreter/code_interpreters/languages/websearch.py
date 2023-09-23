from ..base_code_interpreter import BaseCodeInterpreter
import requests
import os

class WebSearch(BaseCodeInterpreter):
    def __init__(self):
        super().__init__()

    def run(self, search_term):
        bing_search_url = "https://api.bing.microsoft.com/v7.0/search"
        headers = {"Ocp-Apim-Subscription-Key": os.environ['BING_SUBSCRIPTION_KEY']}
        params = {
            "q": search_term,
            "count": 5,
            "textDecorations": True,
            "textFormat": "HTML",
        }
        response = requests.get(
            bing_search_url, headers=headers, params=params  # type: ignore
        )
        response.raise_for_status()
        search_results = response.json()
        for result in search_results["webPages"]["value"]:
            url = result["url"]
            title = result["name"]
            snippet = result["snippet"]
            yield {"output": f"[{title}({url})] {snippet}"}