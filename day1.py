def twoNumberSum(array, targetSum):
    
  d = {}
  for i in range(0, len(array)):
    key = array[i]
    value = targetSum - array[i]
    d.update({key:value})

  for key in array:
    if d[key] in array and key!=d[key]:
  
      return(key, d[key])

if __name__=='__main__':
  print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6],10))