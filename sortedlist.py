from collections import defaultdict 
import itertools

print(sorted([75,86,23,21],reverse=True))
animals =[{'name':'Penguin','age':3},{'name':'lion','age':8},{'name':'elephant','age':5}]
print(sorted(animals, key=lambda animal: animal['age']))

grades = [('ajay',91),('bittu',34),('kamal',40),('ajay',98)]
student_grade = defaultdict(list)
for name,grade in grades:
    student_grade[name].append(grade)
print(student_grade)        

names = ['heena','meena', 'deeka']
print(list(itertools.permutations(names, r=2)))

#how to merge two dictionary
x ={'a':1,'b':2}
y = {'b':3,'c':4}
z = {**x,**y}
print(z)
