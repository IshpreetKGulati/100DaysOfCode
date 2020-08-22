"""
Print all n-digit strictly increasing numbers
Given number of digits n in a number, print all n-digit numbers whose digits are strictly increasing from left to right.
Examples:
Input:  n = 2
Output:  
['01', '02', '03', '04', '05', '06', '07', '08', '09', '12', '13', '14', '15', '16', '17', '18', '19', '23', 
'24', '25', '26', '27', '28', '29', '34', '35', '36', '37', '38', '39', '45', '46', '47', '48', '49', '56', 
'57', '58', '59', '67', '68', '69', '78', '79', '89']

Input:  n = 1
Output: ['01', '02', '03', '04', '05', '06', '07', '08', '09']

"""
from itertools import combinations
def monotonic(i):

    if i == "".join(sorted(i)) :
        return True
    return False

def strictly_increasing(input_number):
    res = []
    numbers = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9", ]

    if input_number == 1:
        for k in range(1, 10):
            res.append("0" + str(k))

    else:
        c = list(combinations(numbers, input_number)) #get all the combinations of length equal to input number

        for comb in c:
            print(comb)
            #append the string to the result list
            if monotonic("".join(comb)):
                res.append("".join(comb)) 

    return res

if __name__ == "__main__":
    input_number = 1
    print(strictly_increasing(input_number))