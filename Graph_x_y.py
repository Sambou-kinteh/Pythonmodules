import re
import matplotlib.pyplot as plt


x_y_cordinates = [10, 20, 30, 40, 50, 100, 200, 500, 1000]

x_values = [363, 882, 1401, 1920, 2439, 5034, 10224, 25794, 51744]


y_values = [378, 918, 1458, 1998, 2538, 5076, 10260, 26028, 52056]

plt.plot(x_y_cordinates, x_values, color = 'teal')

plt.plot(x_y_cordinates, y_values, color = 'red')

plt.show()

print(x_y_cordinates)

print(x_values)

print('\n',y_values)
