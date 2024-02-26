from typing import Union
from fastapi import FastAPI
from fastapi.responses import FileResponse
import serial as sl
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from matplotlib import pyplot as plt
import threading
import time as tim

a = lambda x, y: x * 60 + y

app = FastAPI()
ser = sl.Serial('/dev/ttyUSB0', 9600)

app.add_middleware(
CORSMiddleware,
allow_origins=["*"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

time = []
temperature = []
humidity = []
pressure = []


def read_data():
    data = ser.readline().decode('utf-8').strip()
    data = data.split()
    temperature, humidity, pressure, altitude, rain_val = map(float, data)
    return {'temperature': temperature, 'humidity': humidity, 'pressure': pressure, 'altitude': altitude, 'rain_val': rain_val}

def update_data():
    while True:
        tim.sleep(5)
        try:
            data = read_data()
            temperature.append(data['temperature'])
            humidity.append(data['humidity'])
            pressure.append(data['pressure'])
            time.append(int(datetime.now().timestamp()))    
        except Exception as e:
            print(e)

t = threading.Thread(target=update_data)
t.start()

@app.get("/{stuff}")
async def create_graph(stuff: int):
    print(time)
    plt.plot(time, temperature, label='Temperature')
    plt.plot(time, humidity, label='Humidity')
    plt.plot(time, pressure, label='Pressure')
    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.savefig('graph.png')
    return FileResponse('graph.png')

@app.get("/rain_val/")
async def rain_val():
    rain_val = read_data()['rain_val']
    altitude = read_data()['altitude']
    return {'rain_val': rain_val, 'altitude': altitude}
