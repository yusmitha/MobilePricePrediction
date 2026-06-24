# 📱 Mobile Price Prediction

A machine learning web application that predicts mobile phone price ranges and performs exploratory data analysis (EDA) on mobile phone datasets.

🔗 **Live Demo:** _Coming Soon_

---

## 📌 Overview

This project combines data scraping, data cleaning, exploratory data analysis, and machine learning to predict the price range of mobile phones based on their specifications. It includes a user-friendly web app where users can input mobile features and get instant price predictions.

---

## ✨ Features

- 📊 **Exploratory Data Analysis (EDA)** — Visual insights into mobile phone trends and features
- 🤖 **Price Range Prediction** — ML model predicts whether a phone is budget, mid-range, or high-end
- 🌐 **Web App** — Interactive interface built with Streamlit/Flask
- 🧹 **Data Cleaning Pipeline** — Automated preprocessing pipeline for raw mobile data

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| Pandas | Data manipulation and cleaning |
| Scikit-learn | Machine learning model & pipeline |
| Jupyter Notebook | EDA and model development |
| Streamlit / Flask | Web application framework |

---

## 📁 Project Structure

```
MobilePricePrediction/
│
├── Mobile_df.csv               # Raw dataset
├── Mobile_df_v2.csv            # Cleaned dataset v2
├── Mobile_df_v3.csv            # Cleaned dataset v3
├── Mobile_df_v5.csv            # Final cleaned dataset
│
├── Scrapping.ipynb             # Web scraping notebook
├── Mobile_ML_Data_Cleaning.ipynb  # Data cleaning notebook
├── Mobiles EDA.ipynb           # Exploratory data analysis
│
├── Mobile_Price_Predictor_App.py  # Web app (Streamlit/Flask)
├── pipe.pkl                    # Trained ML pipeline
├── df.pkl                      # Processed dataframe
│
├── requirements.txt            # Python dependencies
├── Procfile                    # Deployment config
└── setup.sh                    # Setup script
```

---

## 🚀 Getting Started

### Prerequisites
Make sure you have Python 3.8+ installed.

### Installation

```bash
# Clone the repository
git clone https://github.com/yusmitha/MobilePricePrediction.git

# Navigate to the project directory
cd MobilePricePrediction

# Install dependencies
pip install -r requirements.txt
```

### Run the App

```bash
# For Streamlit
streamlit run Mobile_Price_Predictor_App.py

# For Flask
python Mobile_Price_Predictor_App.py
```

---

## 📊 Model Info

- **Algorithm:** Scikit-learn ML Pipeline
- **Input:** Mobile phone specifications (RAM, battery, camera, storage, etc.)
- **Output:** Price range category (Budget / Mid-range / High-end)

---

## 👩‍💻 Author

**Yusmitha Lekha**
- GitHub: [@yusmitha](https://github.com/yusmitha)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
