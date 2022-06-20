'''
Search Suggestions System
You are given an array of strings products and a string searchWord.
Design a system that suggesta at most three product names from products after each character of searchWord is typed. 
Suggested products should have common prefix with searchWord. If there are more than three products with a comon prefix return the
three lexicographically (alphabet order) minimums products
return a list of lists of the suggested products offer each character of searchWord is typed

'''
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"

def suggestedProducts(products,searchWord):
    res=[]
    products.sort() #'mobile', 'moneypot', 'monitor', 'mouse', 'mousepad']
    
    l,r = 0, len(products)-1
#    i=0
    for i in range(len(searchWord)):
        c = searchWord[i]
        
        while l<=r and (len(products[l])<=i or products[l][i]!=c):
            l+=1
        while l<=r and (len(products[l])<=i or products[r][i]!=c):    
            r-=1
        res.append([]) #cumulative add
        remain = r-l+1
        for j in range(min(3,remain)):
            res[-1].append(products[l+j])
            
    return res

suggestedProducts(products,searchWord)

res[-1]
res.append([])
res.append([])
res[-1].append(1)
[[],[1]]

'''
