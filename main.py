''' 
cloudy-day: 0
rainy-day: 1
clear-day: 2
windy-day: 3
'''

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from threading import Thread
from datetime import datetime   
import serial as sl
import time

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

app  = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

data = [
]

features = pd.read_csv('chennai 2023-01-01 to 2024-02-27.csv')
labels = np.array(features['cloudcover'])
features= features.drop(['name', 'datetime', 'snow', 'snowdepth', 'sunrise', 'sunset', 'conditions', 'description', 'icon', 'stations', 'cloudcover', 'solarenergy', 'tempmax', 'tempmin', 'feelslikemax', 'feelslikemin', 'feelslike', 'dew', 'precip', 'precipprob', 'precipcover', 'windgust', 'windspeed', 'winddir', 'visibility', 'solarradiation', 'uvindex', 'severerisk', 'moonphase'], axis = 1)
feature_list = list(features.columns)
features = np.array(features)
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.1, random_state = 80)
rf = DecisionTreeRegressor(random_state = 80)
rf.fit(train_features, train_labels)

features_2 = pd.read_csv('chennai 2023-01-01 to 2024-02-27.csv')
labels_2 = np.array(features_2['icon'])
features_2 = features_2.drop(['name', 'datetime', 'snow', 'snowdepth', 'sunrise', 'sunset', 'conditions', 'description', 'icon', 'stations', 'cloudcover', 'solarenergy', 'tempmax', 'tempmin', 'feelslikemax', 'feelslikemin', 'feelslike', 'dew', 'precip', 'precipprob', 'precipcover', 'windgust', 'windspeed', 'winddir', 'visibility', 'solarradiation', 'uvindex', 'severerisk', 'moonphase'], axis = 1)
feature_list_2 = list(features_2.columns)
features_2 = np.array(features_2)
train_features_2, test_features_2, train_labels_2, test_labels_2 = train_test_split(features_2, labels_2, test_size = 0.1, random_state = 80)
rf_2 = DecisionTreeRegressor(random_state = 80)
rf_2.fit(train_features_2, train_labels_2)

def get_time():
    curr = time.time()
    return time.ctime(curr)

def get_cloud_cover(temperature, humidity, pressure):
    val = rf.predict([[temperature, humidity, pressure]])
    val = int(val[0])
    return val

def get_weather(temperature, humidity, pressure):
    val = rf_2.predict([[temperature, humidity, pressure]])
    val = int(val[0])
    return val

def update_data():
    while True:
        try:
            ser = sl.Serial('/dev/ttyUSB0', 9600)
            d = list(map(float, ser.readline().decode('utf-8').split()))
            data.append({
                "temperature": d[0],
                "humidity": d[1],
                "pressure": d[2],
                "altitude": d[3],
                "rain_val": d[4],
                "name": datetime.now().strftime("%H:%M:%S"),
                "mytime": get_time(),
                "cloud_cover": get_cloud_cover(d[0], d[1], d[2]),
                "weather": get_weather(d[0], d[1], d[2])
            })
            #print(data)
            time.sleep(1)
        except Exception as e:
            print(e)

t = Thread(target=update_data)
t.start()

@app.get("/")
def root():
    return {"message": "Hello World"}   

@app.get("/data")
def get_data():
    return data[-6:]
