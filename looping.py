# -*- coding: utf-8 -*-
num1=100
num2=200

if(num1>num2):
    print('num1 is greater')
else:
    print('num2 is greater')
print('iam not a part of if else block')

std = int(input('enter our std'))
if( std==1 ):
    print('your in 1st std')
elif (std ==2 ):
    print('your in 2nd std')
elif(std ==3):
    print('your in 3rd std')
else:
    print('you are in other than above std')

#while
start=1
end=10

while(start<end):
    print(start)
    start=start+1

for i in range(10):
    print (i)
for i in range(10,20):
    print(i)
for i in range(10,20,2):
    print(i)
for i in range(20,10,-1):
    print(i)
    
