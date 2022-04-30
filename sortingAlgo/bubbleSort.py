from pickle import TRUE


def swap(a,i,j):
   a[i],a[j]=a[j],a[i]



a=[2,3,5,3,9,4,2,5,1,7,8,4]
b=[2,3,5,3,9,4,2,1,7,8,4]
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if(a[i]<a[j]):
            print("swaping",a[i]," ",a[j])
            swap(a,i,j)

print("array \n",a)
y=sorted(b,reverse=True)
print("inbuild sort",b,y)

