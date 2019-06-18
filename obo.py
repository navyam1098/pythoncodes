# -*- coding: utf-8 -*-
class student():
    def register(self,regnum,name,std,sec):
        self.regnum=regnum
        self.name=name
        self.std=std
        self.sec=sec
    
    
    def info(self):
        print('Regnum:',self.regnum,'NAME:',self.name,'STD:',self.std,'SEC:',self.sec)
        
navya=student()
navya.register(88,'Navya','3','B')
navya.info()


priyanka=student()
priyanka.register(112,'Priyanka','3','B')
priyanka.info()

class calcy():
    def add(self,num1,num2):
        self.num1=num1
        self.num2=num2
        return num1+num2
    
    def sub(self,num1,num2):
        self.num1=num1
        self.num2=num2
        return num1-num2
    
    def multiply(self,num1,num2):
        self.num1=num1
        self.num2=num2
        return num1*num2
    
    def division(self,num1,num2):
        self.num1=num1
        self.num2=num2
        if num2==0:
            print('impossible')
        else :
            return num1/num2
   
        
n=calcy()
n.division('10','20')
result=n.division(10,20)
print('addition',result)

           
    
    
    



