p=True
q=True
result = not(p or not q)
print (result)

print(".................")
p=True
q=False
print(p)
print(q)
print(".................")
p=False
q=True
print (p)
print (q)
print(".................")
p=False
q=False
print (p)
print (q)
print(".................")

n=123
print ((n%10)/10)
print ((n//10)%10)
print ((n%100-n%10)/10)
print (8%3)
print (5/2)
x=1
y=2
print (x==y)
print (10- -2)
print (x=x==x)

def do_stuff():
    print ("Hello world")
    return ("Is it over yet?")
    print ("Goodbye cruel world!")
    
print (do_stuff())
