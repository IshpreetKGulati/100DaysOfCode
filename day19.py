"""
Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.
Sample Input -> Output
rotate2('Hello') → 'lloHe'
rotate2('java') → 'vaja'

"""
def rotated_left_2(string):
	#since we have to move the first two characters to the end, so we slice the string starting from the third character to the end and 
	#concatinate it to the first two characters.
  return(string[2::]+string[0:2:])
  
string = input()
x = rotated_left_2(string)
print(x)