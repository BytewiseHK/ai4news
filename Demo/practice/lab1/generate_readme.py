import requests

KEY_PATH = "key.md"
DOC_PATH = "doc.md"
OUTPUT_PATH = "readme.md"
API_URL = "https://newsapi.org/v2/everything"

# Read API key
def read_api_key():
    with open(KEY_PATH, "r", encoding="utf-8") as f:
        return f.read().strip()

# Fetch sample news articles
def fetch_news(api_key, query="news", page_size=3):
    params = {
        "q": query,
        "apiKey": api_key,
        "pageSize": page_size
    }
    response = requests.get(API_URL, params=params, timeout=10)
    response.raise_for_status()
    return response.json()

# Generate README with sample articles
def generate_readme(news_data):
    lines = [
        "# NewsAPI Services Overview\n",
        "This README includes sample news articles fetched from NewsAPI.\n",
        "## Sample Articles\n"
    ]
    for i, article in enumerate(news_data.get("articles", []), 1):
        lines.append(f"### Article {i}\n")
        lines.append(f"- **Title:** {article.get('title')}")
        lines.append(f"- **Source:** {article.get('source', {}).get('name')}")
        lines.append(f"- **Author:** {article.get('author')}")
        lines.append(f"- **Published At:** {article.get('publishedAt')}")
        lines.append(f"- **Description:** {article.get('description')}")
        lines.append(f"- **URL:** {article.get('url')}\n")
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

if __name__ == "__main__":
    api_key = read_api_key()
    news_data = fetch_news(api_key)
    generate_readme(news_data)
    print(f"README generated at {OUTPUT_PATH}")
