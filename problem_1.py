#traversing an array
def traversal(b):
    print('[',end="")
    for i in range(len(b)-1):
        print(b[i],end=", ")
    print(b[-1],end=']')
#inserting an element
def insert(ele,ind,arr):
    a1=[0 for i in range(len(arr)+1)]
    for i in range(0,ind):
        a1[i]=arr[i]
    for i in range(ind,len(arr)):
        a1[i+1]=arr[i]
    a1[ind]=ele
    print(a1) 
a=list(map(int,input("enter elements:").split(",")))
traversal(a)
print()
a=insert(10,2,a)