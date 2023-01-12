import streamlit as st
import pandas as pd
import numpy as np
from sktime.forecasting.exp_smoothing import ExponentialSmoothing
from sktime.forecasting.model_selection import temporal_train_test_split
from sktime.metrics.forecasting import smape_loss
import matplotlib.pyplot as plt

st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")

st.title('Building Temperature and Humidity Forecasting')

# Generate sample data
np.random.seed(0)
date_rng = pd.date_range(start='1/1/2020', end='12/31/2020', freq='H')
temp_sensor1 = np.random.randint(low=20, high=40, size=(len(date_rng)))
temp_sensor2 = np.random.randint(low=20, high=40, size=(len(date_rng)))
humidity_sensor1 = np.random.randint(low=20, high=90, size=(len(date_rng)))
humidity_sensor2 = np.random.randint(low=20, high=90, size=(len(date_rng)))
data = pd.DataFrame(date_rng, columns=['date'])
data['temp_sensor1'] = temp_sensor1
data['temp_sensor2'] = temp_sensor2
data['humidity_sensor1'] = humidity_sensor1
data['humidity_sensor2'] = humidity_sensor2

# Filter data by date range
st.header('Filter Data')
start_date = st.date_input('Start Date', value=data['date'].min())
end_date = st.date_input('End Date', value=data['date'].max())
filtered_data = data[(data['date'] >= start_date) & (data['date'] <= end_date)]

# Plot temperature and humidity
st.header('Temperature and Humidity')
temp_sensor = st.selectbox('Select Temperature Sensor', ['temp_sensor1', 'temp_sensor2'])
humidity_sensor = st.selectbox('Select Humidity Sensor', ['humidity_sensor1', 'humidity_sensor2'])
st.line_chart(filtered_data[['date', temp_sensor, humidity_sensor]])

# Plot temperature histogram
st.header('Temperature Histogram')
temp = filtered_data[temp_sensor]
st.hist(temp, bins=20, range=[temp.min(), temp.max()])

#Forecast Temperature
st.header('Forecast Temperature')
y = filtered_data[temp_sensor]
X_train, X_test, y_train, y_test = temporal_train_test_split(X=filtered_data, y=y, test_size=0.2)
forecaster = ExponentialSmoothing(trend='add', seasonal='multiplicative')
forecaster.fit(y_train)
y_pred = forecaster.predict(fh=len(y_test))

# Plot forecasted temperature
st.line_chart(pd.DataFrame({'date': X_test['date'], 'temp': y_test, 'temp_forecast': y_pred}))