a=[-1,2,4,-3,5,2,-5,2]
max_sum=0
sum=0
for i in range(0,len(a)):
    sum=max(a[i],a[i]+sum)
    max_sum=max(max_sum,sum)
print("max subarray is", max_sum)

