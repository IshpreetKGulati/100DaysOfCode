"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.
Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:
Will share image in whatsapp group

Note:
The total number of elements of the given matrix will not exceed 10,000
"""

def return_diag(input_matrix):

  if len(input_matrix) == 0:
    return []
  n = len(input_matrix) #rows
  m = len(input_matrix[0]) #columns
  i = j = 0
  res = []
  up = True #to check if we have to print from up to down or vice vera
  
  #iterate from 0 to total number of diagnols i.e. sum of rows and column
  for _ in range(0, n + m):
    
    if up:
    	# add all the elements in the diagnol to the list till we reach the first row and last column
      while i >= 0 and j < m :
        res.append(input_matrix[i][j])
        i -= 1
        j += 1

      #set the points i and j 
        
      if i < 0 and j<= m-1:
        i = 0
      if j == m:
        j -= 1
        i += 2
      up = False 

    else:
    	#daignol elements to be printed from bottom to up till we reach the last row and first column
      while i < n and j >=0:
        res.append(input_matrix[i][j])
        i += 1
        j -= 1
    
    #set pints i and j
      if j < 0 and i <= n-1:
        j = 0
      if i == n:
        i -= 1
        j += 2
        
      up = True
    
  return res
if __name__ == "__main__":
  input_matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
  ]
  print(return_diag(input_matrix))




