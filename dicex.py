dic = {'a1':'anshul','a2':'anshul','a3':'neha'}
# creating a new dictionary 
my_dict ={"java":100, "python":112, "c":112} 
  
# list out keys and values separately 
key_list = list(my_dict.keys()) 

val_list = list(my_dict.values()) 
uniquevalues = set(my_dict.values())

for values in uniquevalues:
    print(values)
    
         


  
# one-liner 
print(list(my_dict.keys())[list(my_dict.values()).index(112)])
  
