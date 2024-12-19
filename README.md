# Stock Price Prediction 
This is a machine learning-powered application built with Python and Streamlit for stock price prediction. It uses an LSTM (Long Short-Term Memory) neural network to forecast stock prices, enabling investors to make informed decisions based on data-driven insights.

<br><h3>Key Features</h3>
* 📈 Interactive Web Interface: Built with Streamlit for a seamless and user-friendly experience.
- 💹 Real-Time Stock Data: Fetches historical and real-time financial data using YFinance.
- 🤖 LSTM-Based Prediction Model: Utilizes an advanced LSTM neural network for accurate stock price forecasting.
- 📊 Dynamic Visualizations: Leverages Plotly for interactive and visually engaging stock data charts.

<br><h3>How It Works</h3>
- Enter Stock Symbol: User inputs a stock ticker (e.g., AAPL, MSFT, TSLA).
- Fetch Historical Data: Retrieve past stock price data using YFinance.
- Train the LSTM Model: Process and train the data using the LSTM neural network.
- Generate Forecasts: Predict future stock prices for the next several days.
- Visualize Results: Display historical trends and predicted prices on interactive charts.

<br><h3>Tech Stack</h3>
- Python: Core programming language.
- Streamlit: For building the app's interactive interface.
- YFinance: To retrieve stock market data from Yahoo Finance.
- TensorFlow/Keras: For implementing and training the LSTM model.
- Plotly: For creating dynamic and interactive visualizations.

<br><h3>Installation</h3>
- Clone the repository : git clone https://github.com/yourusername/stock-price-prediction.git
                         cd stock-price-prediction
- Install the required dependencies : pip install -r requirements.txt
- Run the app : streamlit run app.py

