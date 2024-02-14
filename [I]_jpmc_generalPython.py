

a=[1,2]
b=a
b[1] = -2
a[1]+b[1]

=-4


a=[1,2]
b=a.copy()
b[1] = -2
a[1]+b[1]

=0

a=(1,2)
a[1]=0
a

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-7-b825ca15754f> in <module>
      1 a=(1,2)
----> 2 a[1]=0
      3 a

TypeError: 'tuple' object does not support item assignment
  
  
  
  ###### Q1 ######
# Write a function that prints a dictionary where keys are between 1 and 20 and their 
# corresponding values are the square of the keys

Def dict():
    A={}
     A = {x: x**2 for x in range(20)}
print(A)



###### Q2 ######
# Output all numbers between 0 and 100 that are divisible by 2 and 5, using list comprehension.

Def all():
    res=[]
    For i in range(100):
        If i%2==0 and i%5 ==0:
        res.append(i)
    Return res

    

###### Q1 ######
# Write a function that prints a dictionary where keys are between 1 and 20 and their corresponding values are the square of the keys

Def dict():
    A={}
    for i in range(1,21):
        A[i] = i**2
    return A
dict()

#A = {x: x**2 for x in range(20)}

---

###### Q2 ######
# Output all numbers between 0 and 100 that are divisible by 2 and 5, using list comprehension.

Def all():
    res=[]
    For i in range(100):
        If i%2==0 and i%5 ==0:
        res.append(i)
    Return res
    
    
    
a = [x for x in range(10)]
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

b = {x:None for x in range(10) }
'''
{0: None,
 1: None,
 2: None,
 3: None,
 4: None,
 5: None,
 6: None,
 7: None,
 8: None,
 9: None}
'''

[x for x in range(100) if x%5==0 and x%2==0]
#[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

[x if x%5==0 and x%2==0 else None for x in range(100)]
#[0,None,None,None,None,None,None,None,None,None,10........]

