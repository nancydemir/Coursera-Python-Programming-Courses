p=True
q=True
result = not(p or not q)
print (result)
p=True
q=False
result = not(p or not q)
print (result)
p=False
q=True
result = not(p or not q)
print (result)
p=False
q=False
result = not(p or not q)
print (result)
