import kivy
kivy.require('2.2.1')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.network.urlrequest import UrlRequest

#import solar_energy
#import cloud_cover
#import icon

import serial as sl

ser = sl.Serial('/dev/ttyUSB0', 9600)

def get_data():
    data = ser.readline().decode('utf-8').strip()
    data = data.split()
    return data

class ViewPlot(GridLayout):
    def __init__(self):
        super(ViewPlot, self).__init__()

    def plot(self):
        #import hardware_data
        '''try:
            while True:
                data = get_data()
                
                temperature.append(float(data[0]))
                humidity.append(float(data[1]))
                pressure.append(float(data[2]))
                
                array = np.array([temperature[-1], humidity[-1], pressure[-1]/10000]).reshape(1, -1)
                
                time_stamp_val = ((datetime.now().strftime('%H:%M:%S')).split(':'))
                
                for i in range(len(time_stamp_val)):
                    time_stamp_val[i] = int(time_stamp_val[i])
                    time_stamp_val = (time_stamp_val[0]*60) + time_stamp_val[1] + (time_stamp_val[2]/60)
                    time_stamp.append(time_stamp_val)
            
                if len(time_stamp) > 10:
                    time_stamp.pop(0)
                    temperature.pop(0)
                    humidity.pop(0)
                    pressure.pop(0)
                
                for ax in axs:
                    ax.clear()
 
                axs[0].plot(time_stamp, temperature, 'r', label='Temperature')
                axs[0].set_title('Temperature')

                axs[1].plot(time_stamp, humidity, 'b', label='Humidity')
                axs[1].set_title('Humidity')
 
                axs[2].plot(time_stamp, pressure, 'g', label='Pressure')
                axs[2].set_title('Pressure')

                plt.text(0.5, 0.95, datetime.now().strftime('%Y-%m-%d %H:%M'), ha='center', va='cent    er', transform=axs[0].transAxes)
                plt.text(0.5, 0.95, datetime.now().strftime('%Y-%m-%d %H:%M'), ha='center', va='cent    er', transform=axs[1].transAxes)
                plt.text(0.5, 0.95, datetime.now().strftime('%Y-%m-%d %H:%M'), ha='center', va='cent    er', transform=axs[2].transAxes)
 
                plt.pause(0.01)
 
                time.sleep(1)

        except KeyboardInterrupt:
            ser.close()
            print('Serial port closed')
            plt.close()
            print('Plot closed')'''

class MyApp(App):
    def build(self):
        return ViewPlot()

if __name__ == '__main__':
        MyApp().run()
