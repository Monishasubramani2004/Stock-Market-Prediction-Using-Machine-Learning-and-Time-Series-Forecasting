from flask import Flask, render_template, request, redirect, url_for, session
from prophet import Prophet
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Dummy user database (replace with a real database in production)
users = {
    'user1': 'password1',
    'user2': 'password2'
}

def fetch_stock_data(ticker):
    """Fetch historical stock data using yfinance."""
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1mo")  # Fetch data for the last month
        data = data.reset_index()

        # Ensure the 'Date' column is a datetime object
        data["Date"] = pd.to_datetime(data["Date"])

        # Remove timezone from the 'Date' column
        data["Date"] = data["Date"].dt.tz_localize(None)

        return data[["Date", "Open", "High", "Low", "Close"]]
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

def predict_stock_price(ticker, periods=30):
    """Predict stock prices using Facebook's Prophet."""
    # Fetch historical data
    df = fetch_stock_data(ticker)

    # Check if the dataset has sufficient data
    if df is None or len(df) < 2:
        raise ValueError(f"Insufficient data for ticker: {ticker}. Please check the ticker symbol or try a different exchange (e.g., RELIANCE.NS for NSE).")

    # Train the Prophet model
    model = Prophet()
    model.fit(df.rename(columns={"Date": "ds", "Close": "y"}))

    # Make future predictions
    future = model.make_future_dataframe(periods=periods, include_history=False)  # Exclude historical data

    # Generate forecast
    forecast = model.predict(future)

    # Ensure we return exactly the number of periods requested
    return forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].head(periods)

def get_investment_advice(current_price, predicted_price):
    """Determine investment advice based on current and predicted prices."""
    if predicted_price > current_price:
        return "It might be a good time to invest, as the price is predicted to rise."
    elif predicted_price < current_price:
        return "It might not be a good time to invest, as the price is predicted to fall."
    else:
        return "The price is predicted to remain stable. Consider other factors before investing."

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            error_message = "Invalid username or password"
            return render_template("login.html", error_message=error_message)
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users:
            error_message = "Username already exists"
            return render_template("register.html", error_message=error_message)
        else:
            users[username] = password
            session['username'] = username
            return redirect(url_for('home'))
    return render_template("register.html")

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route("/", methods=["GET", "POST"])
def home():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == "POST":
        ticker = request.form["ticker"]
        periods = int(request.form["periods"])
        try:
            # Fetch historical data for the candlestick chart
            historical_data = fetch_stock_data(ticker)
            if historical_data is None:
                raise ValueError(f"Unable to fetch historical data for {ticker}.")

            # Generate candlestick chart
            candlestick_chart = create_candlestick_chart(historical_data)

            # Predict future prices
            forecast = predict_stock_price(ticker, periods=periods)
            stock = yf.Ticker(ticker)
            current_price = stock.history(period="1d")["Close"].iloc[-1]
            predicted_price = forecast["yhat"].iloc[-1]
            advice = get_investment_advice(current_price, predicted_price)
            dates = forecast["ds"].dt.strftime('%Y-%m-%d').tolist()
            prices = forecast["yhat"].tolist()

            return render_template(
                "result.html",
                ticker=ticker.upper(),
                forecast=forecast.to_dict("records"),
                dates=dates,
                prices=prices,
                advice=advice,
                candlestick_chart=candlestick_chart
            )
        except ValueError as e:
            error_message = str(e)
            return render_template("index.html", error_message=error_message)
    return render_template("index.html")

def create_candlestick_chart(data):
    """Create a candlestick chart using Plotly."""
    candlestick = go.Candlestick(
        x=data['Date'],
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        name="Candlestick"
    )

    layout = go.Layout(
        title="Candlestick Chart",
        xaxis=dict(title="Date"),
        yaxis=dict(title="Price (USD)"),
        template="plotly_dark"
    )

    fig = go.Figure(data=[candlestick], layout=layout)
    return fig.to_html(full_html=False)

if __name__ == "__main__":
    app.run(debug=True)