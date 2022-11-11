# sentence shortening by word substitutions with synonyms (syns)

# Example: "Walking in the park is nice regardless if alone or not"
# Len 64
# Synonyms: wonderful → pretty/nice, whether → if, regardless → either
# Rewrite 1: "Walking in the park is wonderful either if alone or not"]
# Len 60

s = "Walking in the park is wonderful regardless whether alone or not"

# # Step 1: define a data structure for the synonyms
syns={'wonderful':['pretty','nice'], 'whether':['asif', 'if'], 'alone': ['lonely'] }

key_to_value_len = {k:[len(v) for v in v] for k, v in syns.items()}
min(syns.get('wonderful',0))
#'nice'
syns.get('whether',0)
#['asif', 'if']
max(syns.get('whether',0))
#'if'
len(syns['wonderful'])
#2
syns['wonderful'][0]
#'pretty'
def ss1(s: str, syns:  Dict, tl: int):  # len(output) <= tl
    s = s.split(" ")
    #s = ['Walking', 'in'
    res = []
    final_outcome = []
    for i in syns:
      syns[i] = min(syns.get(i,0))
      #syns - {'wonderful': 'nice', 'whether': 'asif', 'alone': 'lonely'}
    for i in s:
      if i in syns:
        if len(i) < len(syns[i]):
          res.append(i)
        else:
          i = syns[i]
          res.append(i)
      else:
        res.append(i)
        
        
    res = " ".join(res)
    if len(res) <= tl:
      return " ".join(res)
    return
          
