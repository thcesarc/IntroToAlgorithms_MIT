def selection_sort(array):
  selection_sort_recursive(array,len(array))

def selection_sort_recursive(array,index):
  #base case
  #find biggest element
  #swap
  #call for length-1
  if index != 0 :
    max_index = find_max_index(array,index-1)
    swap_to_end(array, max_index,index-1)
    selection_sort_recursive(array,index-1)

def find_max_index(array,index):
  max   = array[0]
  max_index = 0
  for i in range(index+1):
    if(array[i] > max):
      max   = array[i]
      max_index = i
  return max_index

def swap_to_end(array , max_element_index,index):
  temp = array[index]
  array[index] = array[max_element_index]
  array[max_element_index] = temp