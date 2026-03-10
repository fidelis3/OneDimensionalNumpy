#Uses linspace() function to plot 
import numpy as np # type: ignore
 #To generate 5 equally spaced numbers between -2 and 2
x = np.linspace(-2, 2, num=5)
print(x)

#To generate 10 equally spaced numbers between -2 and 2
x = np.linspace(-2, 2, num=10)
print(x)

#We can use the function linspace to generate 100 evenly spaced samples from the interval 0 to 2π:
x = np.linspace(0, 2 * np.pi, num=100)
print(x)

y=np.sin(x)
print(y)