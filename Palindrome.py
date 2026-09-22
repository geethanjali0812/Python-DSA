def palindrome(a):
   l=0
   r=len(a)-1
   for i in range(len(a)//2):
       if a[l]==a[r]:
           return 'yes palindrome'
       else:
           return -1
def reverse(a):
   l=0
   r=len(a)-1
   for i in range(len(a)//2):
       temp=a[l]
       a[l]=a[r]
       a[r]=a[l]
       l+=1
       r-=1
   return a

a=[1,2,3,4,5]
print(reverse(a))


print(palindrome(a))


def substring(s):
   ind={}
   ml=0
   start=0
   for i in range(len(s)):
       if s[i] in ind:
           start=ind[s[i]]+1
       ind[s[i]]=i
       ml=max(ml,i-start+1)
   return ml
s=print(substring("ramcharan"))


def max_sub(a,k):
  result=[]
  for i in range(len(a)-k+1):
    b=a[i]>a[i+1]
    result.append(b)
  return result
a=[1,3,-1,-3,5,3,6,7]



def max_sub(a,k):
  result=[]
  for i in range(k,len(a)+1):
    result.append(max(a[i-k:i]))
  return result
def maximum(a,st,end):
  max=0
  for i in range(st,end):
    if max<a[i]:
      max=a[i]
  return max
print(max_sub(a,3))
