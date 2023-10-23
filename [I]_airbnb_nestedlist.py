'''
Airbnb - interview


# Please join the video conference through the chat window in the bottom right

# boolean has_next()
# return true if there is another element in the whole structure

# int next()
# return the value of the next element in the structure

# int remove()
# remove (from the underlying collection) the last element returned by the iterator and return it.
# That is, remove the element that the previous next() returned
# This method can be called only once per call to next(),
# otherwise an exception will be thrown.
# The behavior of an iterator is unspecified if the underlying
# collection is modified while the iteration
# is in progress in any way other than by calling this method.

 input = [[],[1,2,3],[4,5],[],[],[6],[7,8],[],[9],[10],[]]
# iter = MyIterator(input)
# iter.next() -> 1
# iter.hasNext() -> true
# iter.next() -> 2
# iter.next() -> 3
# iter.remove() -> 3
# print(input) -> [[],[1,2],[4,5],[],[],[6],[7,8],[],[9],[10],[]]
# iter.next() → 4
# input2 = [[5],[4],[3]]
''' 
'''
if type(i) == list:
    numerator += sum(i)
if type(i) == int:
    numerator += i
      
isinstance(i, int)

def l_list(input_list):
    
    for list_integer in input_list:   
#        if isinstance(list_integer, int):
        if type(list_integer)== int:
            _integers.append(list_integer)
        else:
            l_list(list_integer)
    return _integers
            
l_list(input) 
           
_integers[-1]           
input = [[],[1,2,3],[4,5],[],[],[6],[7,8],[],[9],[10],[]]   
def remove(input,x):
    if x in input:
        input.remove(x)
    else:
        for element in input:
            if type(element) == list:
                remove(element,x)
        
remove(input,9)  
'''
input = [[],[1,2,3],[4,5],[],[],[6],[7,8],[],[9],[10],[]]                 
# isinstance(my_variable, int)
class Bolleanhasnext:
    def __init__(self, input):
        self._integers = []
        self._position = -1

#         def l_list(input_list):

#             for list_integer in input_list:   
# #                if isinstance(list_integer, int):
#                 if type(list_integer)==int:                    
#                     self._integers.append(list_integer)
#                 else:
#                     l_list(list_integer)

#         l_list(input)
        self._integers = [item if isinstance(item, int) else i for item in input for i in item]
        #-->[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
    def next(self):
        self._position+=1
        return self._integers[self._position]
      
    def hasNext(self):
        return self._position +1< len(self._integers)
     
    def remove(self):
        def remove2(input):
    
            if self._integers[self._position] in input:     
                input.remove(self._integers[self._position])
            else:
                for element in input:
                    if type(element) == list:
                        remove2(element)
        remove2(input)
        return self._integers[self._position]
       
       
# second alternative option of remove above    
    def delete(self):
        def delete2(input):
            for element in input:
                if type(element) == list:
                    delete2(element)
                else:
                    if self._integers[self._position] in input:
                        input.remove(self._integers[self._position])
        delete2(input)
        return self._integers[self._position]
        
iter = Bolleanhasnext(input)   
print(iter.next())       
print(iter.hasNext())
print(iter.next())
print(iter.next())
print(iter.remove())
print(input)
print(iter.next())
                
