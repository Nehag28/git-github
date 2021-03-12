mid = -1
def search(arr,n):
    i = 0
    l = i;
    u = len(arr)
    for i in range(len(arr)):
        mid = (l+u)//2
        if arr[mid] > n:
            l = 0
            u = mid
        elif arr[mid] < n:
            l = mid
            u = len(arr)
        elif arr[mid]== n:
            globals()['mid'] = mid
            return True
    
          
        
    return False    

arr =[4,7,8,12,45,99]
n=2
if search(arr,n):
    print('found',mid)
else:
    print('not found')