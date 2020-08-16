"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.


Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: True

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: False
"""


def find_target(input_matrix,target):
  
  res = False
  for i in range(0, len(input_matrix)):
    left = 0
    right = len(input_matrix[i])-1
    res = False
    #Binary Search on the inner list
    while(left<=right):
        mid = left + (right-left) // 2
      
        print(input_matrix[i][mid])
        if target == input_matrix[i][mid]:
          return True
        elif target < input_matrix[i][mid]:
          left = mid+1
        elif target > input_matrix[i][mid]:
          right = mid-1
          
  return res
 
if __name__ == "__main__":
  input_matrix = [
  [1,   3,  5],
  [10, 11, 16],
  [23, 30, 34],
 
  ]
  target = 13
  print(find_target(input_matrix,target))




