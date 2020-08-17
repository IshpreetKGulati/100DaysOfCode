"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty-seven is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
Example 1:
Input: 3
Output: "III"
Example 2:
Input: 4
Output: "IV"
Example 3:
Input: 9
Output: "IX"
Example 4:
Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 5:
Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

"""

"""

def num_conversion(input_number):
  s = str(input_number)
  res = ""
  m = 1
  a = []
  
  for _ in range(0, len(s)):
    n = input_number % 10
    a.append(n*m)
    input_number = input_number //10
    m = m*10
  
  for i in range(0,len(a)):
    if i == 0:
      if a[i]<=3:
        res = res + "I" * a[i]
      elif a[i] == 4:
        res = "IV"
      elif a[i] == 5:
        res = "V" + res
      elif a[i] > 5 and a[i]<9:
        res = "V"
        res = res + "I" *(a[i]-5)  
      elif a[i] == 9:
        res = "IX"    
    
    elif i == 1: 
      if a[i]<=30:
        res = "X"*(a[i]//10) + res   
      elif a[i] == 40:
        res = "XL"+res   
      elif a[i] == 50:
        res = "L" + res
      elif a[i]>50 and a[i]<90: 
        res = "X"*((a[i]//10)-5) + res
        res = "L" + res
      elif a[i] == 90:
        res = "XC"+res

    elif i == 2: 
      if a[i]<=300:
        res = "C"*(a[i]//100) + res   
      elif a[i] == 40:
        res = "CD"+res   
      elif a[i] == 500:
        res = "D" + res
      elif a[i]>500 and a[i]<900: 
        res = "C"*((a[i]//100)-5) + res
        res = "D" + res
      elif a[i] == 900:
        res = "CM"+res

    elif i == 3: 
      if a[i]<=3000:
        res = "M"*(a[i]//1000) + res   
      elif a[i] == 40:
        res = "MG"+res   
      elif a[i] == 5000:
        res = "G" + res
      elif a[i]>5000 and a[i]<9000: 
        res = "X"*((a[i]//1000)-5) + res
        res = "L" + res
      elif a[i] == 9000:
        res = "MH"+res
    

  return res

if __name__ == "__main__":
  input_number = 3549
  print(num_conversion(input_number))


"""

def num_conversion(input_number):
  s = str(input_number)
  res = ""
  m = 1
  
  symbols = {1: "I", 5: 'V',
            10: "X", 50:"L",
            100: "C", 500:"D",
            1000:"M" }

  for _ in range(0, len(s)-1): #find the place value of the left most digit
    m = m *10
  
  while input_number > 0:
    n = input_number // m
    if n <= 3:
      res = res + symbols[m] * n 
    elif n == 4:
      res = res + symbols[m] + symbols[m+n*m]

    elif n == 5:
      res = res + symbols[m*n] 
    elif n >5 and n<9:
      res = res + symbols[m*5] + symbols[m] * (n-5) 

    elif n ==9:
      res = res + symbols[m*10-n*m] + symbols[m*10]
    input_number = input_number % m

    m = m//10

  return res

if __name__ == "__main__":
  input_number = 365
  print(num_conversion(input_number))






