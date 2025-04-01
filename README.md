# Wine Quality Prediction

This project uses machine learning to predict the quality of red wine based on its chemical properties. A **Random Forest Classifier** is trained on the **Wine Quality Dataset** to classify wines as **good** or **bad** quality.

## 📂 Dataset
The dataset used in this project is **winequality-red.csv**, which contains 1,599 samples with 12 features:
- Fixed acidity
- Volatile acidity
- Citric acid
- Residual sugar
- Chlorides
- Free sulfur dioxide
- Total sulfur dioxide
- Density
- pH
- Sulphates
- Alcohol
- Quality (target variable)

## 🚀 Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/wine-prediction.git
cd wine-prediction
```

### 2️⃣ Install Dependencies
```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

## 🔍 Usage
### Run the Notebook in Google Colab or Jupyter Notebook
1. Open `wine_prediction.ipynb`.
2. Run all cells step by step.
3. Modify input features to test different wine samples.

### Predict Wine Quality
```python
input_data = (7.3,0.65,0.0,1.2,0.065,15.0,21.0,0.9946,3.39,0.47,10.0)
prediction = model.predict([input_data])
print(prediction)  # Output: 1 (Good Quality) or 0 (Bad Quality)
```

## 📊 Results
- The model achieved **94.06% accuracy** on the test dataset.
- Heatmaps and visualizations provide insights into feature correlations.

## 📌 Features Implemented
✅ Data Preprocessing  
✅ Exploratory Data Analysis (EDA)  
✅ Feature Engineering & Label Binarization  
✅ Train-Test Split  
✅ Model Training using Random Forest  
✅ Accuracy Evaluation  
✅ Predictive System for Wine Quality  

## 🤝 Contributing
Feel free to fork this repository and make improvements. Pull requests are welcome!

## 📜 License
This project is licensed under the MIT License.

