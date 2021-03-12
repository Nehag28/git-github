
numbers = [45,67,22,13,41]
#for i,numbers in enumerate(numbers,start=22):
   # print(i,numbers)
def square(x):
    return x*x

#print(list(map(square,numbers)))    
print([square(x) for x in numbers])

def is_odd(y):
    return bool(y%2)

#print(list(filter(is_odd,numbers)))    
print([y for y in numbers if is_odd(y)])
    
