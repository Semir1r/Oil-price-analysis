import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def prepare_data_for_lstm(brent_file_path, time_steps=1):
    # Load the Brent oil prices data
    brent_data = pd.read_csv(brent_file_path)
    
    # Convert 'Date' column to datetime and set as index
    brent_data['Date'] = pd.to_datetime(brent_data['Date'])
    brent_data.set_index('Date', inplace=True)
    
    # Scale the data to the range [0, 1]
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(brent_data['Price'].values.reshape(-1, 1))
    
    # Prepare the data for LSTM
    X, y = [], []
    for i in range(len(scaled_data) - time_steps):
        X.append(scaled_data[i:(i + time_steps), 0])
        y.append(scaled_data[i + time_steps, 0])
    
    X, y = np.array(X), np.array(y)
    
    # Reshape X to be [samples, time steps, features] for LSTM
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))
    
    return X, y, scaler