# -*- coding: utf-8 -*-

#1find sum of elements in a given list without using builtin functions 
data=[2,4,1,47,38]
print('data')
sum=0
for i in range(0,5):
    sum+=data[i]
print('sum=',sum)
  
#2 max n min of the ellements:
data=[2,4,1,47,38]
for i in range(0,4):
    if(data[i]<data[i+1]):
        t=data[i]
print('minimum value=',t)
data=[2,4,1,47,38]
for i in range(0,4):
    if(data[i]>data[i+1]):
        t=data[i]
print('maximum value=',t)


#3 average of te elements:
data=[2,4,1,47,38]
sum=0
for i in range(0,5):
    sum+=data[i]
    average=sum/len(data)
print('average=',average)
    

#4 element present or wat
n=int(input('enter the number'))
count=0
for i in range(0,4):
    if(data[i]==n):
        count=1
        break 
if(count==1):
    print('present')
else:
    print('absent')



        
        
        
