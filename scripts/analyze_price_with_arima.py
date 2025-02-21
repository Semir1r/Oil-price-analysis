from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt
import pandas as pd


def analyze_brent_prices_with_arima(brent_data, forecast_steps=5):
    # Ensure 'Date' column is in datetime format and set as index
    if 'Date' in brent_data.columns:
        brent_data['Date'] = pd.to_datetime(brent_data['Date'])
        brent_data.set_index('Date', inplace=True)

    # Check for stationarity
    result = adfuller(brent_data['Price'])
    print('ADF Statistic:', result[0])
    print('p-value:', result[1])

    # If not stationary, difference the series
    if result[1] > 0.05:  # p-value greater than 0.05 indicates non-stationarity
        brent_data['Price_diff'] = brent_data['Price'].diff().dropna()
        model_data = brent_data['Price_diff'].dropna()
    else:
        model_data = brent_data['Price']

    # Fit the ARIMA model (adjust p, d, q as needed)
    model = ARIMA(model_data, order=(1, 1, 1))  # Set appropriate orders based on your analysis
    model_fit = model.fit()

    # Forecasting
    forecast = model_fit.forecast(steps=forecast_steps)

    # Plotting the historical prices and forecast
    plt.figure(figsize=(12, 6))
    plt.plot(brent_data.index, brent_data['Price'], label='Brent Oil Price', color='blue')

    # Generate the forecast index
    forecast_index = pd.date_range(start=brent_data.index[-1] + pd.Timedelta(days=1), periods=forecast_steps)

    plt.plot(forecast_index, forecast, label='Forecast', color='red')
    plt.title('Brent Oil Price Forecast using ARIMA Model')
    plt.xlabel('Date')
    plt.ylabel('Price (USD per barrel)')
    plt.legend()
    plt.show()

    return forecast, model_fit  # Return forecasted values and fitted model