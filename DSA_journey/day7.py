#practice problems
#In-place modification
def inplaceMod(nums):
    for i in range(len(nums)):
        nums[i]=nums[i]*2
    print(nums)
nums=[1,2,3,4,5]
print(inplaceMod(nums))
#expected output:[2, 4, 6, 8, 10]