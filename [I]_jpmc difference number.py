ts = [1,3,4,5,6]
first_dts = [2,1,1,1]
a = ts[0]]

def reconstruct(first_dts, a):
  outcome = []
  outcome = a

for i, num in enumerate(first_dts):
  outcome.append(num+outcome[i])
return outcome

reconstruct(first_dts, a)


ts = [1,3,4,5,6]
#first_dts = [2,1,1,1]
second_dts = [-1,0,0]
initial = [ts[1]-ts[0]]

def reconstruct(second_dts, initial):
  second_dts = [-1,0,0]
  initial = [ts[1] - ts[0]]
  for i, num in enumerate(second_dts):
    initial.append(num+initial[i])
  final = [ts[0]]
  for i, num in enumerate(initial):
    fianl.append(num+final[i])
  return fianl
  
reconstruct(second_dts, initial)
#[1,3,4,5,6]



