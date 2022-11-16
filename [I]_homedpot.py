a=[1,2]
b=a
b[1] = -2
a[1]+b[1]


a=[1,2]
b=a.copy()
b[1] = -2
a[1]+b[1]


a=(1,2)
a[1]=0
a

# Time Allowed: ~30 Minutes 

### SQL (1 Question) ###

# Show total cost for each business, sorted from cost highest to lowest.

# Table Business:
# +--------------+------+
# | BusinessName | Cost |
# +--------------+------+
# | Pear         |  100 |
# +--------------+------+
# | Pear         |  175 |
# +--------------+------+
# | Marketplace  |  220 |
# +--------------+------+
# | Horizon      |   50 |
# +--------------+------+
# | Marketplace  |  145 |
# +--------------+------+

# Expected Output:
# +--------------+------+
# | BusinessName | Cost |
# +--------------+------+
# | Marketplace  |  365 |
# +--------------+------+
# | Pear         |  275 |
# +--------------+------+
# | Horizon      |   50 |
# +--------------+------+

Select businessName, sum(cost) as sum_cost
From business
Group by businessName
Order by sum(cost) desc



### Python (3 Questions) ###


###### Q1 ######
# Write a function that prints a dictionary where keys are between 1 and 20 and their corresponding values are the square of the keys

Def dict():
    A={}
     A = {x: x^2 for x in range(20)}
print(A)



###### Q2 ######
# Output all numbers between 0 and 100 that are divisible by 2 and 5, using list comprehension.

Def all():
    res=[]
    For i in range(100):
        If i%2==0 and i%5 ==0:
        res.append(i)
    Return res
    
    
    
a = [x for x in range(10)]

b = {x:None for x in range(10) }
