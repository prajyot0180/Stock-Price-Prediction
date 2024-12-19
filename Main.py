import streamlit as st

st.set_page_config(
    page_title="Stock Prediction App",
    page_icon="😎",
)

st.markdown(
    """# Stock Price Prediction using Machine Learning
### 

**This is  ML-powered stock price prediction app built with Python and Streamlit. It utilizes machine learning models to forecast stock prices and help investors make data-driven decisions.**

Designed and Developed by:

1. Prajyot Uday Pimpale
2. Vaishnavi Vithhal Powar
3. Sakshi Anil Jadhav 
4. Sakshi Shahaji Jadhav

## ️ **How It's Built**

Stockastic is built with these core frameworks and modules:

- **Streamlit** - To create the web app UI and interactivity 
- **YFinance** - To fetch financial data from Yahoo Finance API
- **StatsModels** - To build the ARIMA time series forecasting model
- **Plotly** - To create interactive financial charts

The app workflow is:

1. User selects a stock ticker
2. Historical data is fetched with YFinance
3. ARIMA model is trained on the data 
4. Model makes multi-day price forecasts
5. Results are plotted with Plotly


## **⚖️ Disclaimer**
**This is not financial advice! Use forecast data to inform your own investment research. No guarantee of trading performance.**
"""
)
