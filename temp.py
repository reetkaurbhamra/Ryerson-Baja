'''
import serial
#import matplotlib.pyplot 

arduino = serial.Serial(port='COM3', baudrate=9600)
def read():
    data = arduino.readline()
    return data
while True:
    print(read())
'''
from socket import timeout
import serial
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation



fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

arduino = serial.Serial(port='COM3', baudrate=9600, timeout = .1)
'''
while True:
	data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
	if data:
		print(data)
'''

def animate(i, xs, ys):

    # Read temperature (Celsius) from TMP102
    temp_c = arduino.readline()[:-2] #the last bit gets rid of the new-line chars

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.2%f'))
    ys.append(temp_c)

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Gear Box Temperature')
    plt.ylabel('Temperature (deg C)')

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()     