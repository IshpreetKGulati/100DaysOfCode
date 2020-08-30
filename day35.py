"""
def dfs_path(r,sum,sum_val,input_matrix, count):
    if sum == sum_val:
      count[0] += 1
    if 2*r + 1 < len(input_matrix) and input_matrix[2*r +1] != None:
      dfs_path(2*r + 1, sum+ input_matrix[2*r +1],sum_val,input_matrix, count)
    if 2*r + 2 < len(input_matrix) and input_matrix[2*r +2] != None:
      dfs_path(2*r + 2,  sum+ input_matrix[2*r +2],sum_val,input_matrix, count)
    return count[0]

def sum_tree(input_matrix,sum_val):
  count = [0]
  for i in range(0, len(input_matrix)):
    count1 = dfs_path(i,input_matrix[i],sum_val,input_matrix,count)
 
  return count1
if __name__ == "__main__":
  input_matrix = [10,5,-3,3,2,None,11,3,-2,None,1]
  sum_val = 8
  print(sum_tree(input_matrix,sum_val))

"""

def dfs_path(r,sum,sum_val,input_matrix, count):

    if sum == sum_val:#terminating condition
      count[0] += 1
    if 2*r + 1 < len(input_matrix) and input_matrix[2*r +1] != None: #left node
      dfs_path(2*r + 1, sum+ input_matrix[2*r +1],sum_val,input_matrix, count)
    if 2*r + 2 < len(input_matrix) and input_matrix[2*r +2] != None: #for right node
      dfs_path(2*r + 2,  sum+ input_matrix[2*r +2],sum_val,input_matrix, count)
    return count[0]

def sum_tree(input_matrix,sum_val):
  count = [0]
  for i in range(0, len(input_matrix)):
    res = dfs_path(i,input_matrix[i],sum_val,input_matrix,count)
  return res
if __name__ == "__main__":
  input_matrix = [10,5,-3,3,2,None,11,3,-2,None,1]
  sum_val = 8
  print(sum_tree(input_matrix,sum_val))




