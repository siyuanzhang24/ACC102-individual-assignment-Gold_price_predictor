# 🏅 ACC102: Gold Price Predictor

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://acc102-individual-assignment-goldpricepredictor-sbtscx4v7dnm5y.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

An interactive web application for predicting gold price movements based on macroeconomic factors. Built for ACC102 Mini Assignment (Track 4).

## ✨ Features

- **Interactive Interface**: User-friendly Streamlit app with sliders for USD Index, Treasury Yield, and Inflation Rate
- **Real-time Prediction**: Instant probability calculation of gold price increase
- **Scenario Analysis**: Preset market scenarios (Bullish, Bearish, Neutral, Crisis)
- **Visual Analytics**: Feature importance charts and sensitivity analysis
- **Trading Recommendations**: BUY/HOLD/SELL suggestions with confidence levels

## 📁 Project Structure
ACC102-individual-assignment-Gold_price_predictor/
├── gold_streamlit_app2.py # Main Streamlit application
├── Data and model.ipynb # Jupyter Notebook for data & modeling
├── gold_price_model.pkl # Trained logistic regression model
├── feature_scaler.pkl # Feature scaler for standardization
├── gold_price_dataset_2016_2026.csv # Generated monthly data (2016-2026)
├── requirements.txt # Python dependencies
├── README.md # This file
└── assets/ # Visualizations
├── gold_price_analysis.png
├── correlation_heatmap.png
└── model_evaluation_plots.png
## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository**
bash
git clone https://github.com/siyuanzhang24/ACC102-individual-assignment-Gold_price_predictor.git
cd ACC102-individual-assignment-Gold_price_predictor
2. **Install dependencies**
bash
pip install -r requirements.txt
3. **Run the application**
bash
streamlit run gold_streamlit_app2.py
4. **Open your browser** at `http://localhost:8501`

## 📊 Model Details

### Data
- **Time Period**: 2016-2026 (monthly data)
- **Source**: Synthetic data with realistic patterns
- **Features**:
  - `gold_price`: Gold price in USD/oz
  - `usd_index`: USD Index (negative correlation with gold)
  - `treasury_yield`: 10-Year Treasury Yield (%) - opportunity cost
  - `inflation_rate`: Inflation Rate (%) - inflation hedge

### Model
- **Algorithm**: Logistic Regression
- **Target**: Binary classification (1=price increase, 0=price decrease)
- **Accuracy**: 0.520 (52.0%)
- **ROC AUC**: 0.591

### Key Findings
- USD Index has strongest negative impact on gold price
- Inflation rate shows positive correlation (gold as inflation hedge)
- Treasury yield shows expected negative correlation (opportunity cost)

## 🎮 How to Use

1. **Adjust Input Parameters** (left sidebar):
   - USD Index (80-120, default: 100)
   - Treasury Yield (0-8%, default: 3.5%)
   - Inflation Rate (0-10%, default: 2.5%)

2. **Use Preset Scenarios** (optional):
   - Bullish: Low USD, High Inflation
   - Bearish: High USD, High Rates
   - Neutral: Average Market
   - Crisis: Low Rates, High Inflation

3. **Click "Predict"** to see results:
   - Probability of price increase
   - Predicted direction (Increase/Decrease)
   - Trading recommendation
   - Feature importance visualization

## 📈 Live Demo

[Click here to try the live application](https://acc102-individual-assignment-goldpricepredictor-sbtscx4v7dnm5y.streamlit.app/)

*Note: The application is hosted on Streamlit Cloud and accessible 24/7.*

## 📄 Documentation

- **Demo Video**: [https://github.com/siyuanzhang24/ACC102-individual-assignment-Gold_price_predictor/blob/main/ACC102%20demo%20video.mp4]
- **Reflection Report**: [https://view.officeapps.live.com/op/view. aspx?src=https://raw.githubusercontent. com/siyuanzhang24/
acc102-individual-assignment-gold_price predictor/refs/heads/main/reflection report.docx&wdorigin=browselink]
- **Assignment Requirements**: ACC102 Mini Assignment Track 4

## 🛠️ Technologies Used

- **Frontend**: Streamlit
- **Backend**: Python
- **Data Processing**: pandas, NumPy
- **Machine Learning**: scikit-learn
- **Visualization**: Matplotlib, Seaborn
- **Model Persistence**: joblib
- **Version Control**: Git, GitHub
- **Deployment**: Streamlit Cloud

## ⚠️ Limitations

1. **Educational Purpose**: This tool is for educational demonstration only
2. **Synthetic Data**: Based on generated data with theoretical relationships
3. **Model Simplicity**: Uses linear logistic regression
4. **Market Realities**: Does not account for sudden geopolitical events
5. **Not Financial Advice**: Results should not be used for actual trading

## 🤝 Contributing

This is a course project and not currently accepting contributions.

## 📄 License

This project is licensed under the MIT License.

## 👤 Author

**Siyuan Zhang**
- GitHub: [@siyuanzhang24](https://github.com/siyuanzhang24)
- ACC102 Mini Assignment - Track 4

## 🙏 Acknowledgments
