import re
hand = open('regex_sum_199793.txt')

newlist=list()
count=0
for line in hand:
    
    item = re.findall('[0-9]+', line)
    for i in item:
        #print (newlist)  
        newlist.append(int(i))
        count+=1   
    sum_of_all_numbers=sum(newlist)   
print('num of values: ',count)   
print("sum is:", sum_of_all_numbers)
    

