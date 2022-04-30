a=[6,5,4,6,3,2,6,7,8,9,0,9,7,5,3]

def merge(a,L,R):
    k=0
    temp=[]
    while(len(L)>0 and len(R)>0):
        if(L[0]>R[0]):
            a[k]=R[0]
            R.pop(0)
            k=k+1
        else:
            a[k]=L[0]
            L.pop(0)
            k=k+1
    while(len(L)>0):
        a[k]=L[0]
        L.pop(0)
        k=k+1
    while(len(R)>0):
        a[k]=R[0]
        R.pop(0)
        k=k+1
    


def mergeSort(a):
    if(len(a)>1):
        mid=len(a)//2
        L=a[:mid]
        R=a[mid:]
        print("array",a)
        print("left",L)
        print("right",R)
        mergeSort(L)
        mergeSort(R)
        merge(a,L,R)


mergeSort(a)
print(a)