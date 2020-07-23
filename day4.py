"""
Four Number Sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
The function should find all quadruplets in the array that sum up to the largest sum and return a two dimensional array of all these
quadruplets in no particular order.
"""
def fourNumberSum(array, target):
  answer = []
  array.sort()
 
  for j in range(0, len(array) ):
    num1 = array[j]
    temp1 = target - array[j]
    for i in range(j+1, len(array)):
     
      num2 = array[i]
      temp = temp1 - array[i] 
     
      l = i + 1
      r = len(array) - 1
      while l < r:
        if array[l] + array[r] == temp:
          answer.append([num1, num2, array[l], array[r]])
          l+=1
        if array[l] + array[r] < temp:
          l += 1
        else:
          r -= 1
  return(answer)
  
  
if __name__ == "__main__":
  array = [7,6,4,-1,1,2]
  targetSum = 16
  output = fourNumberSum(array, targetSum)
  print(output)
  