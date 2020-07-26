"""
Monotonic Array
Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.
An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non -decreasing.

Sample Input:
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
Sample Output:
True

"""
"""
def monoArray(array):
    if array == sorted(array):
      return (True)
    elif array == sorted(array, reverse = True):
      return (True)
    else:
      return(False)


if __name__ == "__main__":
  array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
  print(monoArray(array))
"""

def monoArray(array):
  inc = 0
  dec = 0 
  
  for i in range(0, len(array)-1):
    if array[i] < array [i+1] :
      inc +=1
      if dec != 0: # if at any point the array starts showing the behaviour of increasing order, then it it not monotonic, hence return false
        return False
    elif array[i] > array [i+1]:
      dec += 1
      if  inc != 0: # if at any point the array starts showing the behaviour of decreasing order, then it it not monotonic, hence return false
        return False
  

  return True

if __name__ == "__main__":
  array = [1, 1, 5, 6, 7]
  print(monoArray(array))

