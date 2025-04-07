## 📰 Fake News Classification using Machine Learning


## 📌 Overview

In an era of rapid information spread, **distinguishing between fake and real news** has become crucial. This project applies **machine learning techniques** to classify news articles as either **REAL** or **FAKE**, helping fight misinformation using intelligent systems.

## 🚀 Project Highlights

- ✅ Data Cleaning and Preprocessing
- ✅ Exploratory Data Analysis (EDA)
- ✅ Feature Extraction using **TF-IDF**
- ✅ Model Building using:
  - Logistic Regression
  - PassiveAggressiveClassifier
- ✅ Evaluation using Accuracy, Confusion Matrix, and F1 Score
- ✅ Interactive analysis with Jupyter Notebook

## 📂 Dataset

- **Source:** [Kaggle - Fake and Real News Dataset](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset)
- Consists of:
  - \`text\`: News content
  - \`label\`: REAL or FAKE

## 🧠 Technologies Used

| Tool/Library       | Description                          |
|--------------------|--------------------------------------|
| Python             | Programming language                 |
| Pandas & Numpy     | Data manipulation and numerical ops  |
| Scikit-learn       | Machine Learning algorithms          |
| Matplotlib & Seaborn| Data visualization                  |
| TF-IDF Vectorizer  | Text to numerical feature extraction |

## 📊 Model Performance

| Model                     | Accuracy   |
|---------------------------|------------|
| Logistic Regression       | ✅ ~98%     |
| Passive Aggressive Classifier | ✅ ~96% |

> 📌 Logistic Regression showed better accuracy and generalization.

## 📁 Project Structure


📦 Fake-News-Classifier
├── fake_news_classification.ipynb
├── dataset.csv
├── README.md
└── requirements.txt


## ▶️ How to Run

1. Clone the repo  
   \`\`\`bash
   git clone https://github.com/your-username/Fake-News-Classifier.git
   cd Fake-News-Classifier
   \`\`\`

2. Install dependencies  
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. Launch the notebook  
   \`\`\`bash
   jupyter notebook fake_news_classification.ipynb
   \`\`\`

## 🎯 Future Work

- 🧠 Implement Deep Learning (LSTM, BERT)
- 🌐 Deploy as a Web App using Streamlit/Flask
- 📱 Develop a browser extension for real-time detection

## 💡 Inspiration

This project was developed as a practical application of machine learning to address a real-world problem: **fake news detection**, which has critical implications in media, politics, and society.

## 🤝 Contributing

Feel free to fork the repo, raise issues, or submit PRs. Let’s make the internet a more truthful place together!

## 📜 License

MIT License – do anything with the code, just give credit.

