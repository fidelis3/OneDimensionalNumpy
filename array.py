import numpy as np 
a = np.array([0, 1, 2, 3, 4])
a[1]
a[2]=10

#Slicing
a[0:2]=[5, 6]
print(a[1])
print(a)


#To get type of array
print(type(a))
#To get type of values stored in array
print(a.dtype)