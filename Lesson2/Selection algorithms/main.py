from bubblesort     import bubble_sort
from selectionsort  import selection_sort
from mergesort      import *

from numpy import random as rnd
rnd.seed(rnd.randint(10))
#tests:

#BUBBLE SORT
#iterates a one by one comparison and 
#changes only a element position by 1
#at a time
#########################################
array = rnd.randint(0,1000,10)          #
print('initial array:  ', array)        #
bubble_sort(array)                      #
print('bubble sort  :  ',array,'\n')    #
#########################################

#SELECTION SORT
#recursevely inserts the greater element 
#at the end of the array
#########################################
array = rnd.randint(0,1000,10)          #
print('initial array:  ', array)        #
selection_sort(array)                   #
print('selection sort: ',array,'\n')    #
#########################################
                  
#MERGE SORT
#recursively splits the array in smaller
#ones. 
#########################################
array = rnd.randint(0,1000,10)          #
print('initial array:  ', array)        #
merge_sort(array)                       #
print('selection sort: ',array,'\n')    #
#########################################
