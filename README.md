
# 1. Title : Stock-Market-Prediction-Using-Machine-Learning-and-Time-Series-Forecasting

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

## 11. Deployment (Local System)

To set up and run this project on your local machine after cloning it from GitHub, follow these steps:

### 11.1: Prerequisites

* **Git:** Ensure Git is installed on your system. You can download it from [git-scm.com](https://git-scm.com/downloads).
* **Python 3:** This project requires Python 3. You can download it from [python.org](https://www.python.org/downloads/).

### 11.2.1: Clone the Repository

Open your terminal or command prompt and clone the project from GitHub. 

```bash
git clone https://github.com/Monishasubramani2004/Stock-Market-Prediction-Using-Machine-Learning-and-Time-Series-Forecasting.git

```


### 11.2.2 Navigate into the Project Directory

```bash
cd your-repository-name  # e.g., cd Stock-Market-Prediction-ML-TimeSeries
```

---

#### 11.2.3 Create and Activate a Python Virtual Environment

```bash
# Create the virtual environment
python -m venv venv

# Activate the virtual environment:
# On Windows:
.\venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

> You’ll see `(venv)` at the beginning of the terminal prompt when the environment is active.

---

#### 11.2.4 Install Project Dependencies

```bash
pip install -r requirements.txt
```

---

#### 11.2.5 Run the Flask Application

```bash
python app.py
```

---

#### 11.2.6 Access the Application

Visit the following URL in your browser:

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

You should now see the **Stock Market Prediction Using Machine Learning and Time Series Forecasting** app running.

---

### 11.3 Important Notes

* **`app.secret_key`:** In `app.py`, `app.secret_key` is currently set to `'your_secret_key'`. Change it to a unique, secure value for real-world usage.
* **Dummy User Auth:** The app uses a dictionary for user authentication. Replace this with a database like SQLite or PostgreSQL in production.
* **Stopping the Server:** Press `Ctrl + C` in the terminal to stop the Flask app.
* **Deactivating Virtual Environment:**

```bash
deactivate
```

---

### Screenshots:

#### Register:

<img width="1919" height="1033" alt="Register" src="https://github.com/user-attachments/assets/71abd4f7-9e80-448f-bdf0-4a2dac042206" />

#### Login:

<img width="1919" height="969" alt="Login" src="https://github.com/user-attachments/assets/f323ec1a-09b5-4f2d-91ec-3aeefd83ec99" />

#### Dashboard:

<img width="1919" height="976" alt="Dashboard" src="https://github.com/user-attachments/assets/32dc85f9-359d-4ba8-a717-dddd739fb1b3" />

#### Result:

<img width="1919" height="1033" alt="Result" src="https://github.com/user-attachments/assets/f3bcf1cc-5542-432b-8562-dc029de68489" />

#### Investment Advice:

<img width="1163" height="369" alt="Advice" src="https://github.com/user-attachments/assets/62d6084e-d075-49d2-b826-374ca091470f" />


