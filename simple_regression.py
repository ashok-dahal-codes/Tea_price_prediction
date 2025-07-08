import numpy as np
x = np.array([50,60,80,100])
print(f"The existing volumes of tea in ml is {x}")
y = np.array([25,30,35,75])
print(f"the price for the respective existing volumes of tea in ml is {y}")
n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x*y)
sum_xsquared = np.sum(x**2)

m = (n*sum_xy  - sum_x*sum_y)/(n*sum_xsquared - sum_x ** 2)
c = (sum_y - m*sum_x)/n

x_new = int(input("Enter the new volume of tea: "))
y_new = m*x_new + c

print(f"if the volume is {x_new} the price should be {y_new:.2f} ")
