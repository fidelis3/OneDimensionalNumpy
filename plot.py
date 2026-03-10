# Import the libraries

import time 
import sys
import numpy as np  # type: ignore

import matplotlib.pyplot as plt # type: ignore


def Plotvec2(a,b):
    ax = plt.axes()# to generate the full window axes
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)#Add an arrow to the  a Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)#Add an arrow to the  b Axes with arrow head width 0.05, color blue and arrow head length 0.1
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)
    plt.show()#to display the plot


a=np.array([4, 0])#to create a numpy array with values [4, 0]
b=np.array([0, 4])#to create a numpy array with values [0, 4]    

Plotvec2(a,b)#to call the function Plotvec2 with arguments a and b