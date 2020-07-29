"""
Ceasar Cipher Encryptor
Given a non-empty string of lowercase letters and a non-negative integer representing a key, Write a function that returns a new string obtained by shifting any letter in the input string by k positions in the alphabet, where k is the key. Note that letters should "wrap" around the alphabet; in other words, the letter "z" shifted by one returns the letter "a"
Sample Input:
string = "xyz"
key = 2

Sample Output:
"zab"

Optimal Space & Time Complexity
O(1) & O(n), where n is the length of the input string. 

"""

def caesarCipherEncryptor(string, key):
  n = len(string)
  if key > 26:  #if key is greater than 26 then take the mod of key with 26 (26 is the total number of alphbet in english language)
      key = key % 26

  for i in range(0, len(string)):
    new_position = (ord(string[i]) + key) #the new position that is the cipher text value is the current position incremented by the key value
    
    if new_position > ord("z"): #if the cipher value is greter than the ascii value of "z" 
      new_position = ord("a") + new_position - ord("z") - 1 #find the actual position by taking its difference with the ascii value of z and adding it to the ascii value of "a"

    string += chr(new_position)

  return(string[n:len(string):]) 

string = "xyz"
key = 2
print(caesarCipherEncryptor(string, key))
