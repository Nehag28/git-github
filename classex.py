
class car:

    wheels = 5
    def __init__(self,comp,price):
        self.comp = comp
        self.price = price

    def config(self,comp,price):
        print(comp,price)
    @classmethod 
    def info(cls):
        return cls.wheels
    @staticmethod    
    def inval():
        print("hello class") 

    


c1 = car('honda', 5000)
c1.config('maruti',2000)
print(c1.comp)       
print(car.wheels)
print(car.info())
car.inval()