"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

def dfs (i, j,  input_matrix):

  n = len(input_matrix)
  m = len(input_matrix[0])

  #terminating condition
  if i  >= n or j  >= m or i < 0 or j < 0 or  input_matrix[i][j] != "1":
    return
  
  input_matrix[i][j] = "2" #mark the visited matrix as 2
  
  #update the row and column to check top, bottom, left and right elements
  row = [1,-1,0,0]
  col = [0,0,1,-1]
  
  #call dfs for all the four adjacent elements
  for k in range(0,4):
    dfs(i +row[k], j+col[k],input_matrix)


def count_island(input_matrix):
  n = len(input_matrix) #number of rows
  m = len(input_matrix[0])#number of columns
  count = 0

  for i in range(0, n):
    for j in range(0, m):
      if input_matrix[i][j] =="1":

      	#call the function for each i,j pair if the element is 1 and increment the count by 1
        dfs(i,j,input_matrix)
        count +=1

  return count

if __name__ == "__main__":
  input_matrix = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
  ]
  print(count_island(input_matrix))
