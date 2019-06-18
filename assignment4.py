# -*- coding: utf-8 -*-
class car():
    def __init__(self,make,model,color,price):
        self.make=make
        self.model=model
        self.color=color
        self.price=price
        self.speed=0
  
    def start(self):
        self.speed=0
        print('speed is 0 when you start the car',self.speed)
        
    def move(self):
        self.speed+=5
        print('speed of car while moving =',self.speed)
        
    def stop(self):
        self.speed=0
        print('speed is 0 when you stop the car',self.speed)
        
    def info(self):
        print('make',self.make,'model',self.model,'color',self.color,'price',self.price)
        


specification.info()
specification.start()
specification.move()
specification.stop()
specification=car('hero','duet','pearl white',55000)






































    

