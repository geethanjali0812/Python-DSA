#practice problems
#In-place modification
def inplaceMod(nums):
    for i in range(len(nums)):
        nums[i]=nums[i]*2
    print(nums)
nums=[1,2,3,4,5]
inplaceMod(nums)
#expected output:[2, 4, 6, 8, 10]


#Matrix Traversal
def maxTraversal(matrix):
    row=len(matrix)
    col=len(matrix[0])
    for i in range(row):
        for j in range(col):
            print(matrix[i][j])
matrix=[[1,2,3],[4,5,6],[7,8,9]]
maxTraversal(matrix)

#Matrix sum
def matrixSum(matrix):
    Sum=0
    for row in matrix:
        for val in row:
            Sum+=val
    print(Sum)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
matrixSum(matrix)