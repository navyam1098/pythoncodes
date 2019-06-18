# -*- coding: utf-8 -*-

for j in range(10,0,-1):
   
        print('12', '*' , j ,'=', j*12)

#2
def si(p,t,r):
    s=(p*t*r)/100
   
    return s
p=int(input('enter the principle'))
t=int(input('enter the time'))
r=int(input('enter te rate'))
s=si(p,t,r)
print(s)

#3
n1=int(input('enter n1'))
n2=int(input('enter n2'))

for i in range(n1 ,n2):
    if i>1:
     
    if (i % n) == 0: 
               break
           else: 
              print(i) 
      
# Find & Displaying Fibonacci series   
a, b = 0, 1
while a <10:
     print(a)
     a, b = b, a+b      
     i = 0


