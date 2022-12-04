##########################################
#Question 2:
#Given a data structure D supporting the four first/last sequence operations:
#D.insert first(x), D.delete first(), D.insert last(x), D.delete last(),
#each in O(1) time, describe algorithms to implement the following higher-level operations in terms
#of the lower-level operations. Recall that delete operations return the deleted item.
###########################################

#supose the data structure D is a static array
#re-implementing the methods:

class DataStructure:
  def __init__(self,list_of_data):
    self.datas = list_of_data
  
  def insert_first(self,value):
    self.datas[0] = value
  
  def insert_last(self,value):
    self.datas[-1] = value
  
  def remove_first(self):
    value = self.datas[0]
    self.datas[0] = None
    return value
  def remove_last(self):
    value = self.datas[-1]
    self.datas[-1] = None
    return value    

#(a) swap_ends():  Swap the first and last items in the sequence in D in O(1) time.

  def swap_ends(self):
    stored_first_item = self.remove_first()
    self.datas[0]  = self.datas[-1]
    self.datas[-1] = stored_first_item
    
#(b) shift left(D, k): Move the first k items in order to the end of the sequence n D
#in O(k) time.
  def shift_left(self,k):
    if (k < 1) or (k > len(self.datas) -1 ):
        return
    stored_first_item = self.remove_first()
    del self.datas[0]
    self.datas.append(stored_first_item)
    self.shift_left(k-1)

#create object
object_data = DataStructure([1,2,3,4,5,6,7,8,9,10])
#object_data.swap_ends()
print(object_data.datas)
object_data.shift_left(7)
print(object_data.datas)


