# %%
import requests
from bs4 import BeautifulSoup
import os

# %%
def fetch_article_text(source):
    if os.path.isfile(source):
        with open(source, 'r', encoding='utf-8') as f:
            return f.read()
    elif source.startswith("http://") or source.startswith("https://"):
        try:
            response = requests.get(source, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                # Try to extract visible paragraphs from the page
                paragraphs = soup.find_all('p')
                article_text = ' '.join([p.get_text() for p in paragraphs if p.get_text().strip()])
                return article_text.strip()
            else:
                raise Exception(f"Error feteching URL: {response.status_code}")
        except Exception as e:
            print(f"[ERROR] Could not fetech article from URL: {e}")
            return ""
    else:
        print("[ERROR] Invalid input. Please provide a valid file path or URL.")
        return ""

def print_summary(entities, sentiment_map, keywords, timeline):
    print("\n[🧠 Entities Found]")
    for label, items in entities.items():
        print(f"  {label}: {', '.join(items)}")

    print("\n[💬 Entity Sentiment]")
    for entity, score in sentiment_map.items():
        print(f"  {entity}: {score if score is not None else 'N/A'}")

    print("\n[🔥 Top Keywords]")
    print(", ".join(keywords))

    print("\n[🕒 Timeline of Events]")
    for event in timeline:
        print(f"  - {event['date']}: {event['main_action']} → {event['event_summary']}")


# %%



