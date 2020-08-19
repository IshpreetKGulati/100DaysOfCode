"""
Write a Python program of recursion list sum.
Example 1:
Input: grid = [1, 2, [3,4],[5,6]]
Output: 21
"""


def recursive_sum(input_matrix, s = []):
    sum = 0
    for i in input_matrix:
    	# if type of the element in the imout matrix is int, then add it to the sum
    	#else recursivle call the function for the ith element
        if type(i) is int:
            sum += i
        else:
            sum += recursive_sum(i)
    return sum
  
if __name__ == "__main__":
  input_matrix = [[1, 2, 1]]
  print(recursive_sum(input_matrix))




