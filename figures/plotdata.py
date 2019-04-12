import matplotlib.pyplot as plt
import csv
import numpy as np

xdata = []
ydata = []
data = [[],[]]
filename = '22-21-50.csv'
infile = open(filename, 'r')

count = 0
for line in infile:
    num= ''
    for element in line:
        if element != ',':
            num += element
        else:
            data[count].append(int(num))
            num = ''
            continue
    
    count += 1
infile.close()
data[1] = [_/10 for _ in data[1]]
data[0] = [_ if _ > 450 else np.nan for _ in data[0]]

plt.plot(data[1], data[0])
plt.ylabel('Mode position (px)')
plt.xlabel('Time (s)')
plt.show()
