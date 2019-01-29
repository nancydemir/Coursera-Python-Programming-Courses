import re
count=0
hand = open('testfileforassignment2.txt')
sum = 0
for line in hand:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if len(x) > 0:
        for item in x:
            sum += int(item)
    count+=1
print(sum,count)
