def merge_sort(array):
  if len(array)>1 :

    leftarray, rightarray = break_into_smaller_arrays(array)

    merge_sort(leftarray)
    merge_sort(rightarray)

    two_fingers_comparison(array,leftarray,rightarray)

    
    

def break_into_smaller_arrays(array):
  middle = len(array)//2
  leftarray  = array[:middle].copy() #copy() method for error handling when array type equals nparray
  rightarray = array[middle:].copy()
  return leftarray,rightarray

#function name comes after J.Solomon's lecture:
#https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-3-sets-and-sorting/
#at 43:21
def two_fingers_comparison(array, leftarray, rightarray):
  (i,j,k) = (0,0,0)
  while i < len(leftarray) and j < len(rightarray):
      if leftarray[i] <= rightarray[j]:
        array[k] = leftarray[i]
        i=i+1
      else:
        array[k] = rightarray[j]
        j=j+1
      k=k+1
  #remaining items  
  while i < len(leftarray):
      array[k] = leftarray[i]
      i=i+1
      k=k+1
  while j < len(rightarray):
      array[k] = rightarray[j]
      j=j+1
      k=k+1
    