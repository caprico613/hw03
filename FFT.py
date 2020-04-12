import matplotlib.pyplot as plt
import numpy as np
import serial
import time

sample = 100 #data_arr:400, data_format:4, sample = data_arr / data_format
Ts = 0.1; # sampling interval
# Fs = 128.0;  # sampling rate

t = np.arange(0, 10, Ts) # time vector; create Fs samples between 0 and 1.0 sec.
x = [0 for i in range(0, int(sample))]
y = [0 for i in range(0, int(sample))]
z = [0 for i in range(0, int(sample))]
tilted = [0 for i in range(0, int(sample))]

# n = len(y) # length of the signal
# k = np.arange(n)
# T = n/Fs
# frq = k/T # a vector of frequencies; two sides frequency range
# frq = frq[range(int(n/2))] # one side frequency range

# print("gogo\n")

serdev = '/dev/ttyACM0'
s = serial.Serial(serdev, baudrate=115200)
for i in range(0, int(sample)):
    line = s.readline() # Read an echo string from K66F terminated with '\n'
    # print line
    x[i] = float(line)
    line=s.readline() # Read an echo string from K66F terminated with '\n'
    # print line
    y[i] = float(line)    
    line=s.readline() # Read an echo string from K66F terminated with '\n'
    # print line
    z[i] = float(line)    
    line=s.readline() # Read an echo string from K66F terminated with '\n'
    # print line
    tilted[i] = float(line)

fig, ax = plt.subplots(2, 1)
l1, = ax[0].plot(t, x, 'b', label = 'x')
l2, = ax[0].plot(t, y, 'r', label = 'y')
l3, = ax[0].plot(t, z, 'g', label = 'z')
ax[0].legend(loc = 'best')
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Acc Vector')
ax[1].plot(t, tilted, 'b') # plotting the spectrum
ax[1].set_xlabel('Time')
ax[1].set_ylabel('Tilt')

plt.show()
s.close()