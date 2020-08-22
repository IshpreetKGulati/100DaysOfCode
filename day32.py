"""
Power Set in Lexicographic order
This problem is about generating Power set in lexicographical order.
Examples :
Input : abc
Output : ["a","ab","abc","ac","b","bc","c"]

Input : "banana"
Output = ['a', 'aa', 'aaa', 'aaab', 'aaabn', 'aaabnn', 'aaan', 'aaann'
"""

from itertools import combinations
def power_set(input_string):
  #write your code here
  #return all possible outputs in a list
  #res = ["a","ab","abc","ac","b","bc","c"]
  res = set()
  input_string = "".join(sorted(input_string)) # sort the string
  for i in range(1, len(input_string)+1):
    for j in combinations(input_string,i): #get all the combinations
      res.add("".join(j))# add in a set to get all the unique elements only
 
  res = list(res)
  res.sort()
  return res
if __name__ == "__main__":
  input_string = "banana"
  print(power_set(input_string))




