import streamlit as st
import pandas as pd
import numpy as np
import datetime
import requests


st.title("Welcome!")
st.title("Let's predict your taxi fare")
'''
# 🚕 🔮
'''


st.markdown('''#

### Please specify your request:
''')
st.markdown("***")
key = 42


st.markdown('''
### Date and time:
''')
d = st.date_input(
    "Choose a date for your drive",
    datetime.date(2021, 3, 12))
st.write('You chose:', d)

st.markdown('##')

t = st.time_input('Choose a time for your drive', datetime.time(8, 45))

date_time = datetime.datetime.combine(d,t).strftime("%Y-%m-%d %H:%M:%S UTC")

st.write('You chose', t)



st.markdown("***")


st.markdown('''
### Pickup and dropoff details:
''')

pickup_lon = st.number_input('Insert the pickup longitude')
st.write('Your pickup longitude is ', pickup_lon)

st.markdown('##')
pickup_lat = st.number_input('Insert the pickup latitude')
st.write('Your pickup latitude is ', pickup_lat)

st.markdown('##')
dropoff_lon = st.number_input('Insert the dropoff longitude')
st.write('Your dropoff longitude is ', dropoff_lon)

st.markdown('##')
dropoff_lat = st.number_input('Insert the dropoff latitude')
st.write('Your dropoff latitude is ', dropoff_lat)



st.markdown("***")

st.markdown('''### Number of passengers:''')
number_passengers = st.number_input('', min_value=1, max_value=10, value=1, step=1)
st.write('Your number of passengers is ', number_passengers)



url = 'http://taxifare.lewagon.ai/predict_fare/'
params = {'key': key,
          'pickup_datetime': date_time,
          'pickup_longitude': float(pickup_lon),
          'pickup_latitude': float(pickup_lat),
          'dropoff_longitude': float(dropoff_lon),
          'dropoff_latitude': float(dropoff_lat),
          'passenger_count': int(number_passengers)}

prediction = requests.get(url=url, params=params).json()
st.markdown("***")

st.write('## Your predicted fare:')
st.write('##', prediction['prediction'], "$")
