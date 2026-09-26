#maximum subarray
def maximumSubarray(nums):
    current_sum=nums[0]
    max_sum=nums[0]
    for i in nums[1:]:
        current_sum=max(i,current_sum+i)
        max_sum=max(max_sum,current_sum)
    return max_sum

nums=[-2,1,-3,4,-1,2,1,-5,4]
print(maximumSubarray(nums))