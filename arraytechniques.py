def leftshift(key,arr):
  ar=[0 for i in range(len(arr))]
  j=0
  for i in range(key,len(arr)):
    ar[j]=a[i]
    j+=1
  for i in range(0,key):
    ar[j]=a[i]
    j+=1
  print(ar)
    
a=[1,2,3]
a=leftshift(1,a)

# sliding window
def maxi(key,arr):
  sum=0
  for i in range(key):
    sum+=a[i]
  maxavg=sum/key
  for i in range(key,len(arr)):
    sum=sum+a[i]-a[i-key]
    avg=sum/key
    if maxavg<avg:
      maxavg=avg
  print(maxavg)


a=[1,2,3,4,5,6,7]
maxi(3,a)

# average
def average(arr):
  sum=0
  for i in range(0,len(arr)):
    sum+=arr[i]
  avg=sum/len(arr)
  print(avg)
a=[1,2,3]
average(a)

# Problem Summary:
#Given a sorted array, remove duplicate elements in-place so that each unique element appears only once.
# input
class Solution:
    def removeDuplicates(self, n) -> int:
        if not n:
            return 0

        unique_ind = 0

        for i in range(1, len(n)):
            if n[i] != n[unique_ind]:
                unique_ind += 1
                n[unique_ind] = n[i]

        return unique_ind + 1


def main():
    a = int(input())
    n = list(map(int, input().split()))

    sol = Solution()
    k = sol.removeDuplicates(n)

    print(k)
    print(' '.join(map(str, n[:k])))


if __name__ == "__main__":
  main()