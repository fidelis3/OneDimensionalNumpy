import numpy as np
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

#To add two arrays
sum=np.add(arr1,arr2)
print(sum)

#To subtract two arrays
sub=np.subtract(arr1,arr2)
print(sub)

#To multiply two arrays
mul=np.multiply(arr1,arr2)
print(mul)

#To perform division 
div=np.divide(arr2,arr1)
print(div)

#To perform dot product(it multiplies value1 of array1 with value2 of array2 and so on and then adds them)
dot=np.dot(arr1,arr2)
print(dot)