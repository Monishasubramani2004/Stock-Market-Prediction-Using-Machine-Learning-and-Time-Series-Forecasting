
# 1.Title :Stock-Market-Prediction-Using-Machine-Learning-and-Time-Series-Forecasting

---

## 2. Objective / Problem Statement

To forecast future stock prices using historical market data and provide actionable investment advice to reduce risk and support decision-making.

---

## 3. Proposed Solution / Approach

We used the **Facebook Prophet** time-series forecasting algorithm, combined with **rule-based logic**, to predict stock prices from **Yahoo Finance** data. Key preprocessing included handling missing values, resampling data, and feature selection. Predictions were visualized via candlestick charts.

---

## 4. System Architecture / Design

### Modules:

* Data Fetching (yfinance)
* Preprocessing (cleaning, resampling, formatting)
* Forecasting (Facebook Prophet)
* Investment Logic (rule-based decisions)
* Visualization (candlestick charts with Plotly)
* Web Interface (Flask + HTML)

### Flowchart (Brief):

* Input Stock Ticker
* Data Collection
* Preprocessing
* Forecast with Prophet
* Generate Advice
* Visual Output

---

## 5. Tools and Technologies Used

* **Programming Language:** Python
* **Libraries:** Facebook Prophet, Pandas, NumPy, yfinance, Plotly, Requests
* **Frameworks:** Flask, Dash
* **Other Tools:** Holidays, Jupyter Notebook

---

## 6. Key Features / Functionalities

* Fetch historical stock data from Yahoo Finance
* Predict future stock prices (up to 90 days)
* Generate investment advice: Strong Buy, Buy, Hold, or Sell
* Visualize predictions using interactive candlestick charts
* Web interface with login and forecasting form

---

## 7. UI Design Sketch (Optional)

* Login Page
* Input Form for ticker and date range
* Output Page with candlestick chart, forecast table, and investment advice

---

## 8. Challenges Faced

* **Handling Missing Data:** Resolved using forward-fill and resampling
* **Model Accuracy:** Fine-tuned Prophet using cross-validation and real stock datasets
* **Integration:** Ensuring smooth flow from backend forecasting to frontend visualization

---

## 9. Learning Outcomes

* Hands-on experience with **time-series forecasting**
* Practical usage of **Prophet, Flask, and yfinance APIs**
* Skills in **data preprocessing, visualization, and deployment**
* Better understanding of **financial analytics and investment indicators**

---

## 10. Conclusion

Our system successfully predicts stock prices using Facebook Prophet and supports investment decisions via rule-based logic. In the future, we aim to integrate **deep learning models (LSTM, GRU), real-time streaming, and sentiment analysis** to improve accuracy and scope.
