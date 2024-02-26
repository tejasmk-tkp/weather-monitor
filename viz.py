import serial as sl
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import time

ser = sl.Serial('/dev/ttyUSB0', 9600)

def get_data():
    data = ser.readline().decode('utf-8').strip()
    data = data.split()
    return data

time_stamp = list()
temperature = list()
humidity = list()
pressure = list()

fig, axs = plt.subplots(3)
'''for ax in axs:
        ax.legend()'''

try:
    while True:
        data = get_data()
        temperature.append(float(data[3]))
        humidity.append(float(data[1]))
        pressure.append(float(data[2]))
    
        time_stamp_val = ((datetime.now().strftime('%H:%M:%S')).split(':'))
        for i in range(len(time_stamp_val)):
            time_stamp_val[i] = int(time_stamp_val[i])
        time_stamp_val = (time_stamp_val[0]*60) + time_stamp_val[1] + (time_stamp_val[2]/60)
        time_stamp.append(time_stamp_val)

        print(time_stamp, temperature, humidity, pressure)
    
        if len(time_stamp) > 10:
            time_stamp.pop(0)
            temperature.pop(0)
            humidity.pop(0)
            pressure.pop(0)
    
            for ax in axs:
                ax.clear()
    
        axs[0].plot(time_stamp, temperature, 'r', label='Temperature')
        axs[0].set_title('Temperature')
    
        #axs[0].set(xlim=(time_stamp[0]-5, time_stamp[-1]+5), ylim=(temperature[0]-10, temperature[-1]+10))

        axs[1].plot(time_stamp, humidity, 'b', label='Humidity')
        axs[1].set_title('Humidity')
    
        #axs[1].set(xlim=(time_stamp[0]-5, time_stamp[-1]+5), ylim=(humidity[0]-10, humidity[-1]+10))

        axs[2].plot(time_stamp, pressure, 'g', label='Pressure')
        axs[2].set_title('Pressure')
    
        #axs[2].set(xlim=(time_stamp[0]-5, time_stamp[-1]+5), ylim=(pressure[0]-10, pressure[-1]+10))

        plt.tight_layout()
        plt.pause(0.01)
    
        time.sleep(1)

except KeyboardInterrupt:
    ser.close()
    print('Serial port closed')
    plt.close()
    print('Plot closed')
