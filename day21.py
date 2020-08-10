"""
Write a  program to find maximum of each column of  2d array 
Sample Input -> Output
max_col([[1, 5, 13], [11], [9, 18]]) → [11, 18, 13] 
max_col([[1, 8, 1], [1,21], [9]]) → [9, 21, 1]

"""
import itertools 

def max_col(test_list):
  li = list(itertools.zip_longest(*test_list, fillvalue=0))#convert rows to column
  res = list(itertools.starmap(max, li))#find the max row element
  return res
if __name__ == "__main__":
  input_list = [[1, 9, 1], [1,21], [9]]
  print(max_col(input_list))




