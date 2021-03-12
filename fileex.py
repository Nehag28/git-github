f = open("myson.txt",'r')
f1 = open("neha",'w')
#f1.write("hello neha")
for data in f:
    f1.write(data)

f1.close()    
f2 = open('pic.jpg','rb')
f3 = open('mypic.jpg','wb')
for i in f2:
    f3.write(i)