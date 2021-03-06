"""
Smallest Difference   
Write a function that takes in two non-empty arrays of integers, find the pair of numbers (one from each array) whose absolute difference is closet to zero, and returns an array containing these two numbers, with the numbsers, with the number from the first array in the first position.

You can assume that there will only be one pair of numbers with the smallest difference.

Sample Input

arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

Sample Output

[28, 26]

Optimal Solution
O(nlog(n)) + O(mlog(m) + O(m+n))
where,
n is the size of arrayOne
m is the size of arrayTwo
"""

def smallestDifference(arrayOne, arrayTwo):
  min_diff = float('inf')
  answer = []
  arrayOne.sort()
  arrayTwo.sort()

  #For each element in array one, compare the absolute difference between the element from array one and the leftmost element of array two
  #with the absolute difference between the element from array one and the rightmost element
  
  for i in range(0, len(arrayOne)):
    left = 0
    right = len(arrayTwo) - 1
    while left < right:
      if abs(arrayOne[i] - arrayTwo[left]) > abs(arrayOne[i] - arrayTwo[right]):
        left +=1
      else:
        right -=1
    if abs(arrayOne[i] - arrayTwo[right]) < min_diff:
        min_diff = abs(arrayOne[i] - arrayTwo[right])
        answer.append([arrayOne[i], arrayTwo[left]])  
  #print(answer)
  return(answer[len(answer)-1])
    

if __name__ == "__main__":
  arrayOne = [-1, 5, 10, 20, 28, 3]
  arrayTwo = [26, 134, 135, 15, 17]
  print(smallestDifference(arrayOne, arrayTwo))