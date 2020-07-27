"""
Longest Mountain Peak
Given an array arr[] with N elements, the task is to find out the longest sub-array which has the shape of a mountain.
The Longest Peak consists of elements that are initially in ascending order until a peak element is reached and beyond the peak 
element all other elements of the sub-array are in decreasing order.

Input: arr = [2, 2, 2] 
Output: 0 
Explanation: 
No sub-array exists that shows the behaviour of a mountain sub-array.

Input: arr = [1, 3, 1, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5] 
Output: 11 

Explanation: 
There are two sub-arrays that can be considered as mountain sub-arrays. The first one is from index 0 – 2 (3 elements) and next 
one is from index 2 – 12 (11 elements).  As 11 > 2, our answer is 11.

"""

def LongestPeak(a): 

  #dividing the problem in three categories, depending on the length of input array as, since the mininmum lenghth should be 3
  result=0
  m = 0 #counter 
  if len(a) < 3: #if length of array is less than 3 then its is not possible to have a mountain peak
    result = 0

  if len(a) == 3:# if length of array is 3 then if mountain peak exists, then answer should be 3
    for i in range(1, len(a)-1):
     if a[i] > a[i+1] and a[i-1] < a[i]:
        result = 3

  else: # for all arrays of length greater than 3
    for i in range(1, len(a)-1):
      if a[i-1] < a[i] and a[i] < a[i+1]: #if previous element and next element both are in ascending order,a then increment m
        m += 1  

      elif a[i] > a[i+1]: #if  current element is greater than next element then also increment by 1
        m +=1
    
      elif a[i-1] > a[i] and a[i] < a[i+1]:  #if previous element is greater and next element is also greater, then break   
        if m > result: #if m is greter than result, then set result     
          result = m + 1
        m = 1
    if m > result:
      result = m+1
  return result

if __name__ == "__main__":
  d = [ 1, 2, 1 ]
  print(LongestPeak(d))