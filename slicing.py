
#Slicing arrays from  [start:end:step].
import numpy as np  # type: ignore
arr=np.array([ 1, 2, 3, 4,5,6,7])
print(arr[1:5:2])

#slicing from start to the end index
print(arr[:4])

#slicing from start index to the end of array
print(arr[4:])

#If we don't pass step its considered 1

print(arr[1:5:])

#output even numbers
print(arr[1:8:2])

#To determine size of array
print(arr.size)

#To determine number of dimensions
print(arr.ndim)

