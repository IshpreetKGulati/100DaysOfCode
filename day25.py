"""
Given two strings s and t , write a function to determine if t is an anagram of s.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: True

Example 2:
Input: s = "rat", t = "car"
Output: False

"""


def check_anagram(sentence_1,sentence_2):
  res = False
  sentence_1 = set(sentence_1.lower()) #convert sentence to lower case and create a set, to include only unique elements
  sentence_1.discard(" ") #remove the space
  sentence_2 = set(sentence_2.lower()) #convert sentence to lower case and create a set, to include only unique elements
  sentence_2.discard(" ")
  
  if sentence_1 == sentence_2: #compare the two senetences
      res = True
  return res
if __name__ == "__main__":
  sentence_1 = "Ca utio ned"
  sentence_2 = "e d u c a t i o n"
  print(check_anagram(sentence_1,sentence_2))




