#sliding window
#problem 1
n=[1,2,3,4,5]
k=2
def max_sum(n,k):
    window_sum=sum(n[:k])
    maximum=window_sum
    for r in range(k,len(n)):
        window_sum+=n[r]
        window_sum-=n[r-k]
        maximum=max(maximum,window_sum)
    return maximum
print(max_sum(n,k))