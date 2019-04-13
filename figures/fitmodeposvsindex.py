from matplotlib import pyplot as plt
import numpy as np

data  = []
indices = [] 
filename = '18-7-49.csv'
infile = open(filename, 'r')
count = 0
for line in infile:
    num= ''
    for element in line:
        if count == 0:
            if element != ',' and element != 'nan':
                num += element
            else:
                if num == '':
                    data.append(np.nan)
                else:
                    data.append(float(num))
                num = ''
        else:
            if element != ',' and element != 'nan':
                num += element
            else:
                if num == '':
                    indices.append(np.nan)
                else:
                    indices.append(float(num))
                num = ''
    count += 1

plt.plot(indices, data)
plt.title('Mode position vs Chamber index')
plt.ylabel(r'Mode position ($\theta_r$)')
plt.xlabel('Chamber Index')
plt.show()
