import streamlit as st
import json
import os
import time
from datetime import datetime, timedelta
import pytz
import io
import PyPDF2
import pandas as pd
import requests

# 🌑 Enforce Dark Theme
# st.markdown("""
#     <style>
#         body { background-color: #0e1117; color: white; }
#         .stApp { background-color: #0e1117; }
#     </style>
# """, unsafe_allow_html=True)

st.markdown("""
    <style>
        /* Hide Streamlit Branding */
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .viewerBadge_container__1QSob {display: none !important;} 

        /* Hide Profile Picture (Both Sidebar & Main UI) */
        [data-testid="stSidebarUserContent"], 
        [data-testid="stUserAvatar"], 
        [data-testid="stFloatingActionButton"] {
            display: none !important;
        }
    </style>
""", unsafe_allow_html=True)


SCRAPY_PROJECT_DIR = os.path.abspath("news_scraper")
NEWS_FILE = os.path.join(SCRAPY_PROJECT_DIR, "news.json")

IST = pytz.timezone("Asia/Kolkata")

def load_news():
    """Load and sort the latest news from news.json."""
    if os.path.exists(NEWS_FILE):
        with open(NEWS_FILE, "r", encoding="utf-8") as f:
            try:
                articles = json.load(f)
                base_time = datetime.now(pytz.utc)  # Ensure it's in UTC
                for i, article in enumerate(articles):
                    if "discovered" not in article:
                        utc_time = base_time.replace(microsecond=0) - timedelta(seconds=i)
                        ist_time = utc_time.astimezone(IST)  # Convert to IST
                        article["discovered"] = ist_time.strftime("%Y-%m-%d %H:%M:%S IST")
                return articles
            except json.JSONDecodeError:
                return []
    return []

message = """
<div style="
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 40px;
    white-space: nowrap;
    overflow: hidden;
    background: linear-gradient(90deg, #ffcc00, #ff9900);
    color: black;
    font-size: 16px;
    font-weight: bold;
    border-radius: 5px;
    padding: 5px 10px;
">
    <marquee behavior="scroll" direction="left" scrollamount="5">
        📰 News articles are updated every 30 minutes! Stay tuned for the latest updates!
    </marquee>
</div>
"""

# --- Tabs UI ---
tabs = st.tabs(["Latest News", "Chicago News Analysis & Chatbot"])

DEFAULT_API_KEY = "530dec48a9ac4ae5907570f2acf3433a"

with tabs[0]:
    st.markdown(message, unsafe_allow_html=True)
    st.title("📰 AI News Aggregator")
    st.write("### 📰 Latest News Articles")
    news_articles = load_news()
    categories = sorted(set(article.get("category", "Uncategorized") for article in news_articles))
    selected_category = st.selectbox("Select Category", ["All"] + categories)
    search_query = st.text_input("🔍 Search for news topics...")
    filtered_articles = [
        article for article in news_articles
        if (selected_category == "All" or article.get("category") == selected_category) and
           (search_query.lower() in article.get("title", "").lower() or 
            search_query.lower() in article.get("content", "").lower())
    ]
    sort_order = st.radio("Sort by:", ("Newest First", "Oldest First"))
    filtered_articles.sort(
        key=lambda article: datetime.strptime(article.get("discovered", "1970-01-01 00:00:00")[:19], "%Y-%m-%d %H:%M:%S"),
        reverse=(sort_order == "Newest First")
    )
    if not filtered_articles:
        st.info("No matching news found.")
    else:
        for article in filtered_articles:
            st.subheader(article.get("title", "Untitled"))
            st.write(article.get("content", "Content not available."))
            st.write(f"**Category:** {article.get('category', 'Uncategorized')}")
            st.write(f"**Discovered:** {article.get('discovered', 'Unknown')}")
            st.write("---")

def articles_to_lines(articles):
    lines = []
    for a in articles:
        desc = a.get("description", "")
        url = a.get("url", "")
        if url:
            line = f"{desc} [Read more]({url})"
        else:
            line = desc
        lines.append(line)
    return "\n\n".join(lines)

with tabs[1]:
    st.write("## 📄 Chicago News Article Analysis & Chatbot")
    # --- Batch Extraction Section ---
    uploaded_file = st.file_uploader("Upload Chicago Excel file (with Zipcode Level Data)", type=["xlsx"], key="extractor-uploader")
    api_key = DEFAULT_API_KEY
    if uploaded_file:
        df = pd.read_excel(uploaded_file, sheet_name="Zipcode Level Data")
        zipcodes = df['Zipcode'].astype(str).tolist()
        neighborhoods = df['Neighborhood'].astype(str).tolist()

        all_results = []
        with st.spinner("Fetching news..."):
            for neighborhood, zipcode in zip(neighborhoods, zipcodes):
                query = f"{neighborhood} {zipcode} Chicago"
                url = "https://newsapi.org/v2/everything"
                params = {
                    "q": query,
                    "apiKey": api_key,
                    "language": "en",
                    "sortBy": "publishedAt",
                    "pageSize": 2  # Adjust as needed
                }
                r = requests.get(url, params=params)
                articles = r.json().get("articles", [])
                for article in articles:
                    result = {
                        "News Article Link": article.get("url", ""),
                        "News Article Name": article.get("title", ""),
                        "News Article Reported Date and Time": article.get("publishedAt", ""),
                        "News Article Source": article.get("source", {}).get("name", ""),
                        "Place of Crime": f"{neighborhood}, {zipcode}, Chicago",
                        "Police Department Mentioned": "",
                        "Police identified the suspect?": "",
                        "Name of the Suspect": "",
                        "Group": "",
                        "Ethnicity": "",
                        "Age of the Suspect": "",
                        "Date and Time of Crime": "",
                        "Crime Location": "",
                        "What type of Crime Happened?": "",
                        "Gun or Knife Used in this Crime": "",
                        "Arrested?": "",
                        "Charge?": "",
                        "Jailed": "",
                        "Bond Value": "",
                        "Retail store Crime Association": "",
                        "Suspect has the History of Crime": "",
                        "Trial": ""
                    }
                    all_results.append(result)

        if all_results:
            result_df = pd.DataFrame(all_results)
            st.dataframe(result_df)
            towrite = io.BytesIO()
            result_df.to_excel(towrite, index=False, engine='openpyxl')
            st.download_button(
                label="Download as Excel",
                data=towrite.getvalue(),
                file_name="chicago_news_article_analysis.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        else:
            st.info("No news articles found for the uploaded data.")
    st.markdown("---")
    # --- Chatbot Section ---
    st.write("### 🤖 Chicago News Chatbot")
    api_key_chat = DEFAULT_API_KEY  # Use the same key for both
    if api_key_chat:
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []
        user_input = st.text_input("Ask anything about Chicago news:", key="chatbot-input")
        if st.button("Ask", key="chatbot-ask-btn") and user_input:
            # Always include 'Chicago' in the query
            query = user_input if "chicago" in user_input.lower() else f"{user_input} Chicago"
            url = "https://newsapi.org/v2/everything"
            params = {
                "q": query,
                "apiKey": api_key_chat,
                "language": "en",
                "sortBy": "publishedAt",
                "pageSize": 20
            }
            r = requests.get(url, params=params)
            articles = r.json().get("articles", [])
            if articles:
                response_lines = articles_to_lines(articles)
                st.session_state.chat_history.append(("user", user_input))
                st.session_state.chat_history.append(("bot", response_lines))
            else:
                # Fallback: try a more general Chicago news query
                fallback_query = "Chicago news"
                params["q"] = fallback_query
                r = requests.get(url, params=params)
                articles = r.json().get("articles", [])
                if articles:
                    response_lines = articles_to_lines(articles)
                    st.session_state.chat_history.append(("user", user_input))
                    st.session_state.chat_history.append(("bot", response_lines))
                else:
                    st.session_state.chat_history.append(("user", user_input))
                    st.session_state.chat_history.append(("bot", "No relevant news found for your query."))
        # Display chat history
        for speaker, msg in st.session_state.chat_history:
            if speaker == "user":
                st.markdown(f"**You:** {msg}")
            else:
                st.markdown(f"**Bot:** {msg}")

FIELDS = [
    "News Article Link", "News Article Name", "News Article Reported Date and Time", "News Article Source",
    "Place of Crime", "Police Department Mentioned", "Police identified the suspect?", "Name of the Suspect",
    "Group", "Ethnicity", "Age of the Suspect", "Date and Time of Crime", "Crime Location",
    "What type of Crime Happened?", "Gun or Knife Used in this Crime", "Arrested?", "Charge?", "Jailed",
    "Bond Value", "Retail store Crime Association", "Suspect has the History of Crime", "Trial"
]

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_entities(text):
    # Dummy extraction logic, replace with real NLP for production
    result = {field: "" for field in FIELDS}
    # Example: extract date
    import re
    date_match = re.search(r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2}, \d{4}", text)
    if date_match:
        result["News Article Reported Date and Time"] = date_match.group(0)
    # Add more extraction logic here...
    return result
