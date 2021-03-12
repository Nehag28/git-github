hours = int(input('enter the hours='))
    
rate = int(input('enter the rate='))
        
if hours > 40 :
        pay = (40 * rate) + (hours-40)*(rate*1.5)
        print(pay)
else :
        pay = hours * rate
        print(pay)
    






