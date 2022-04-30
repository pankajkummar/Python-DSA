arr = [1,2,5,6,3,7]
for j in range(2, len(arr)):
    key = arr[j]
    i=j-1
    while(i>0 and arr[i]>key):
        arr[i+1] = arr[i]
        i=i-1
    arr[i+1] = key

for i in arr:
    print(i)
    