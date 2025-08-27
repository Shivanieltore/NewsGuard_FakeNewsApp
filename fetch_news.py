import requests
import pandas as pd
import os

# Replace with your own API key from https://newsapi.org
API_KEY = "de546351f5504b13b278f1f332199036"

# Fetch latest top headlines from India
url = f"https://newsapi.org/v2/top-headlines?country=in&pageSize=20&apiKey={API_KEY}"
response = requests.get(url)

if response.status_code != 200:
    print("Failed to fetch news:", response.text)
    exit()

articles = response.json().get("articles", [])
print(f"Fetched {len(articles)} headlines.")

# Extract headlines
headlines = [article["title"] for article in articles if article.get("title")]

# Save to CSV as real news
df = pd.DataFrame({
    "text": headlines,
    "label": [1] * len(headlines)  # Label all as real (1)
})

os.makedirs("dataset", exist_ok=True)
csv_path = "dataset/extra_data.csv"

# Append if file exists, otherwise create
if os.path.exists(csv_path):
    df_existing = pd.read_csv(csv_path)
    df = pd.concat([df_existing, df], ignore_index=True)

df.to_csv(csv_path, index=False)
print(f"Saved headlines to {csv_path}")
