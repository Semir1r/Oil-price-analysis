import numpy as np

def forecast_with_lstm(model, scaler, brent_data, time_steps=1, forecast_steps=5):
    # Create the input for forecasting
    last_data = brent_data['Price'].values[-time_steps:]
    last_data = last_data.reshape(-1, 1)
    last_scaled = scaler.transform(last_data)

    X_forecast = []
    for _ in range(forecast_steps):
        X_forecast.append(last_scaled)
        last_scaled = np.append(last_scaled[1:], [[last_scaled[-1]]]).reshape(-1, 1)
    
    X_forecast = np.array(X_forecast)
    X_forecast = np.reshape(X_forecast, (X_forecast.shape[0], X_forecast.shape[1], 1))
    
    # Make predictions
    predictions = model.predict(X_forecast)
    predictions = scaler.inverse_transform(predictions)  # Reverse scaling

    return predictions