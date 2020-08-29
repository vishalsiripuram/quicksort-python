def Partition(arr,st,end):
    pivot=arr[end]
    Pindex=st
    for i in range(st,end):
        if arr[i]<pivot:
            temp=arr[Pindex]
            arr[Pindex]=arr[i]
            arr[i]=temp
            Pindex+=1
    temp=arr[end]
    arr[end]=arr[Pindex]
    arr[Pindex]=temp
    return Pindex



def quicksort(arr,st,end):
    if st<end:
        pa=Partition(arr,st,end)
        quicksort(arr,st,pa-1)
        quicksort(arr,pa+1,end)
arr=[9,8,5,1,4,10,11,0]
n=len(arr)
quicksort(arr,0,n-1)
print(arr)