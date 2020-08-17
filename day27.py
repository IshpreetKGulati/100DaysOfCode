"""

Given a string s. Return all the words vertically in the same order in which they appear in s.
Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
Each word would be put on only one column and that in one column there will be only one word.
Example 1:
Input: s = "HOW ARE YOU"
Output: ["HAY","ORO","WEU"]
Explanation: Each word is printed vertically. 
 "HAY"
 "ORO"
 "WEU"

Example 2:
Input: s = "TO BE OR NOT TO BE"
Output: ["TBONTB","OEROOE","   T"]
Explanation: Trailing spaces is not allowed. 
"TBONTB"
"OEROOE"
"   T"

"""


def return_vertically(input_string):
  #convert the string to list
  l = input_string.split()
  m = 0
  d = []

  #find the maximum length of the string
  for i in range(0,len(l)):
    a = len(l[i])
    if a > m:
      m = a
  
  # make length of each string in l equal
  for i in range(0,len(l)):    
    l[i] = l[i].ljust(m, " ")
  
  # add each character in column (vertically) wise in a list
  for i in range(0, m):
    s = ""
    for j in range(0, len(l)):
      s = s + l[j][i]
    d.append(s.rstrip())#remove the trailing space
  
  return d
if __name__ == "__main__":
  input_string = "CONTEST IS COMING"
  print(return_vertically(input_string))




