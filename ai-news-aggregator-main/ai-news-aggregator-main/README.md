# 🧠 AI News Aggregator 📰

An **Agentic AI-powered news aggregator** that autonomously collects, analyzes, and summarizes the latest news from around the globe. Built using Python and Streamlit, it delivers real-time updates tailored to user preferences.

---

## 🚀 Features

- 🌍 Global news aggregation via APIs or web scraping
- 🤖 Summarization using LLMs (e.g., GPT-4, Ollama, or OpenAI)
- 📊 Displays clean UI via Streamlit
- 📂 Saves results in structured JSON format
- 🔁 Scheduler for regular updates (via GitHub Actions or local CRON)

---

## 📂 Project Structure

```
.
├── streamlit_app.py          # Main Streamlit UI
├── scraper_runner.py         # Scraping and news aggregation logic
├── news.json                 # Stored news data
├── progress.json             # Tracks scraping progress
├── Requirements.txt          # Python dependencies
├── .devcontainer             # Optional dev container setup
├── .github/workflows         # GitHub Actions for automation
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repo

```bash
git clone https://github.com/<your-username>/ai-news-aggregator.git
cd ai-news-aggregator
```

### 2. Install Dependencies

```bash
pip install -r Requirements.txt
```

### 3. Run the App

```bash
streamlit run streamlit_app.py
```

---

## 📡 Data Sources

- RSS feeds
- APIs (NewsAPI, SerpAPI, or custom scrapers)
- Web scraping using `requests`, `BeautifulSoup`, or Playwright

---

## 🧠 AI Integration

LLM model used for:
- News summarization
- Categorization
- Filtering based on relevance

Supports:
- OpenAI API
- Ollama (local LLM)
- Hugging Face Transformers

---

## 📅 Automation

Includes GitHub Actions workflow:
- `.github/workflows/scraper.yml` → Automatically scrapes and updates news data

---

## 👥 Contributors

| Name            | Role                                   |
|------------------|----------------------------------------|
| **Vinay N**       | Full-Stack Developer & AI Integrator   |
| **Mayur Nayak** | Full-Stack Developer & AI Integrator   |

> Both contributors have contributed equally to this project in terms of development, AI integration, and deployment.

---

## 📝 License

This project is licensed under the **MIT License**.

---

## 🙌 Acknowledgements

- OpenAI for GPT models
- NewsAPI & SerpAPI
- Streamlit for UI framework
- GitHub Actions for automation

---

## 📬 Contact

For inquiries:  
📧 vinayn@email.com 
📧  mrmayurnayak07@gmail.com
