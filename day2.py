"""
Three Number Sum
Write a function that takes in a non empty array of distinct integers and an integer representing a target sum. 
The function should find a list of triplets in the array that sum upto the target sum and return a two-dimensional array of all the these triplets.
The numbers in each triplet should be order in ascending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold.

If no three numbers sum up to the target sum, the function should return an empty array.
"""

def threeNumberSum(array, targetSum):
  d = {}
  l = []
  
  for i in range(0, len(array)):
    key = array[i]
    value = targetSum - array[i]
    d.update({key:value})

  for key in array:
    tar = d[key]

    for i in range(0, len(array)):
      diff = tar - array[i]
      if diff in array and diff != array[i] and key != diff and key != array[i]:
        l.append([key, array[i], diff]) 

    for i in range(0, len(l)):
      l[i].sort()
 
  output = []
  for i in range(0, len(l)):
    if l[i] not in output:
      output.append(l[i])
    output.sort()
  return(output)
  
    
if __name__ == '__main__':
  array =  [12, 2, 1, 3, -6, 5, -8, 6]
  targetSum = 0
  
  print(threeNumberSum(array, targetSum))
  