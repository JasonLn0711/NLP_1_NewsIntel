# main.py
from entity_extractor import extract_entities
from sentiment_analyzer import analyze_entity_sentiment
from summarizer import extract_keywords, build_timeline
from visualizer import generate_wordcloud
from utils import fetch_article_text, print_summary

import sys
import os 
import datetime

def save_output_to_file(content):
    os.makedirs("(output)_NLP_NewsIntel", exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join("(output)_NLP_NewsIntel", f"summary_{timestamp}.txt")    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\n📁 Output saved to: {filepath}")

def main():
    # Example URL or file input
    if len(sys.argv) > 1:
        source = sys.argv[1]
    else:
        source = input("Enter news article URL or local file path: ")

    output_log = []

    print("\n🔄 Loading article...")
    output_log.append("🔄 Loading article...")
    text = fetch_article_text(source)

    print("\n🔍 Extracting entities...")
    output_log.append("🔍 Extracting entities...")
    entities = extract_entities(text)

    print("\n💬 Analyzing sentiment...")
    output_log.append("💬 Analyzing sentiment...")
    sentiment_map = analyze_entity_sentiment(text, entities)

    print("\n🧠 Extracting keywords...")
    output_log.append("🧠 Extracting keywords...")
    keywords = extract_keywords(text)

    print("\n🕒 Building timeline...")
    output_log.append("🕒 Building timeline...")
    timeline = build_timeline(text)

    print("\n🎨 Generating word cloud...")
    output_log.append("🎨 Generating word cloud...")
    generate_wordcloud(keywords)

    print("\n✅ Summary")
    output_log.append("✅ Summary")

    from io import StringIO
    buffer = StringIO()
    original_stdout = sys.stdout
    sys.stdout = buffer
    print_summary(entities, sentiment_map, keywords, timeline)
    sys.stdout = original_stdout

    print(buffer.getvalue())
    output_log.append(buffer.getvalue())
    save_output_to_file("\n".join(output_log))

if __name__ == "__main__":
    main()
