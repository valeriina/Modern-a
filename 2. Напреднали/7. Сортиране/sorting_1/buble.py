arr=[12,3,15,4,8,1.7,10]
print(arr)
for i in range(len(arr)-1,0,-1):
    for j in range(i):
        if arr[j]>arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
    print(arr)
