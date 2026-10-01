#LINEAR SEARCH
def linearsearch(a,target):
  for i in range(len(a)):
    if a[i]==target:
      print(f'{target} is found at index value {i}')
      return
  print("not found")
  return -1
a=[2,3,6,4,10]
linearsearch(a,11)


#BINARY SEARCH
def binarysearch(a,target):
  l=0
  r=len(a)-1
  m=(l+r)//2
  while l<r:
    if a[m]==target:
      print(f'{target} is found at index value {m}')
      return
    elif a[m]<target:
      l=m
      m=(l+r)//2
    else:
      r=m
      m=(l+r)//2
    print("not found")
    return -1
a=[2,3,4,6,7,10]
binarysearch(a,5)


#SELECTION sort
def selectionsort(a):
  for i in range(len(a)):
    min=i
    for j in range(i+1,len(a)):
      if a[j]<a[min]:
        min=j
    a[i],a[min]=a[min],a[i]
  return a
a=[9,3,7,4,10]
print(selectionsort(a))

#BUBBLE sort
def bubblesort(a):
  for i in range(len(a)):
    for j in range(i+1,len(a)):
      if a[i]>a[j]:
        a[i],a[j]=a[j],a[i]
  return a

a=[9,3,7,4,10]
print(bubblesort(a))











