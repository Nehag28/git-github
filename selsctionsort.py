minpos = -1
def ssort(list):
    
  
    for i in range(len(list)-1):
        minpos = i

        for j in range(i,len(list)):
            if list[minpos]>list[j]
                minpos = j

        temp = list[i]
        list[i] = list[minpos]
        list[minpos] = temp
            

list = [2,8,5,9,3]
ssort(list)
print(list)


