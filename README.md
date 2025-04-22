# 🧠 NewsIntel: A Smart News Analyzer with NLP

**NewsIntel** is a modular NLP application that takes in a news article (from a URL or a local text file), extracts named entities, builds a timeline of events, analyzes entity-based sentiment, and generates a keyword cloud — all using Python NLP tools.

---

## 🚀 Features

- ✅ Named Entity Recognition (NER)
- ✅ Entity-Based Sentiment Analysis
- ✅ Keyword Extraction (with Lemmatization & POS filtering)
- ✅ Event Timeline Generation
- ✅ Word Cloud Visualization
- ✅ Supports both **web URLs** and **local `.txt` files**

---

## 📁 Project Structure

```
newsintel/
├── main.py
├── entity_extractor.py
├── sentiment_analyzer.py
├── summarizer.py
├── visualizer.py
├── utils.py
├── requirements.txt
└── README.md
```

---

## 📦 Installation Instructions

### 1. Clone or download the repo
```bash
git clone https://github.com/JasonLn0711/NLP_1_NewsIntel.git
cd NLP_NewsIntel
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

#### Or manually:
```bash
pip install spacy textblob requests beautifulsoup4 matplotlib wordcloud
python -m textblob.download_corpora
python -m spacy download en_core_web_sm
```

---

## 🧪 How to Run

### Option 1: Analyze a news article from a **URL**
```bash
python main.py "https://www.bbc.com/news/articles/clyq0n3em41o"
```

### Option 2: Analyze a **local text file**
```bash
python main.py input/sample_article.txt
```

---

## 🧠 Output Includes

- List of named entities (PERSON, ORG, DATE, etc.)
- Sentiment scores for each entity
- Most relevant keywords (filtered + lemmatized)
- Event timeline (with dates and action verbs)
- Word cloud popup for keyword visualization

---

## 🧊 Sample Output
```
🔄 Loading article...
🔍 Extracting entities...
💬 Analyzing sentiment...
🧠 Extracting keywords...
🕒 Building timeline...
🎨 Generating word cloud...
✅ Summary

📌 Entities:
  PERSON: Elon Musk
  ORG: Twitter
  DATE: 2022
  MONEY: $44 billion

📊 Entity Sentiment:
  Elon Musk: 0.12
  Twitter: -0.05

🔑 Keywords:
acquire, billion, company, launch, Twitter

🕒 Timeline:
  [2022] acquire → Elon Musk acquired Twitter for $44 billion in 2022.
```

---

## 📘 License
MIT

---

## ✨ Future Plans
- [ ] Add PDF/JSON export
- [ ] Add BERT-based NER and sentiment
- [ ] Deploy with a Streamlit or Flask web interface

---

Happy hacking! 🧠💬🚀
