
#Slicing arrays from  [start:end:step].
import numpy as np 
arr=np.array([ 1, 2, 3, 4,5,6,7])
print(arr[1:5:2])

#slicing from start to the end index
print(arr[:4])

#slicing from start index to the end of array
print(arr[4:])

#If we don't pass step its considered 1

print(arr[1:5:])