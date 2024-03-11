import os
import requests

# https://learn.microsoft.com/ja-jp/bing/search-apis/bing-web-search/reference/endpoints

url = "https://api.bing.microsoft.com/v7.0/search"

headers = {
    "Ocp-Apim-Subscription-Key": os.environ["BING_SUBSCRIPTION_KEY"],
}

payload = {"q": "What's the most favorite Generative AI?", "mkt": "ja-JP"}

resp = requests.get(url, params=payload, headers=headers)

print(resp.json())
