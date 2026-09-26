#subarray sum equals k
def subarraySum(nums,k):
    prefix_sum=0
    count=0
    prefix_map={0:1}
    for i in nums:
        prefix_sum+=i
        required_ele=prefix_sum-k
        if required_ele in prefix_map:
            count+=prefix_map[required_ele]
        prefix_map[prefix_sum]=prefix_map.get(prefix_sum,0)+1
 
    return count
    
    
    


nums=[1,2,3]
k = 3
print(subarraySum(nums,k))