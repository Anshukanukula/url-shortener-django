import requests

response = requests.post(
    "http://127.0.0.1:8000/shortener/create/",
    json={"original_url": "https://openai.com"}
)

print("Response:", response.json())
