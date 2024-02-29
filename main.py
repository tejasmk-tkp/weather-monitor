from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from threading import Thread
from datetime import datetime   
import serial as sl
import time

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
                "rain_value": d[4],
                "name": datetime.now().strftime("%H:%M:%S")
            })
            print(d)
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

