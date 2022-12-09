#input:  array
#output: sorted array
def bubble_sort(array):
  for j in range(len(array)-1):
    for i in range(len(array)-1-j):
      if array[i+1] < array[i]:
        temp      = array[i]
        array[i]  = array[i+1]
        array[i+1]= temp