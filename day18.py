"""
Given 2 sets of integers,  M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  M or N  but do not exist in both.

Input Format
The first line of input contains an integer, M.
The second line contains M space-separated integers.
The third line contains an integer, N.
The fourth line contains N space-separated integers.

Output Format
Output the symmetric difference integers in ascending order, one per line.

Sample Input
4
2 4 5 9
4
2 4 11 12
Sample Output
5
9
11
12
"""


"""
#without sets
def symmetric_diff(m, array1, n, array2):
    ans = []
	
	# find the elements present in array1 and not in array 2 excluding the common elements
    for i in range(0 ,m):
        present_in_both = False
        left = 0
        right = n- 1
        while left < right:
            if array1[i] == array2[left] or array1[i] == array2[right]:
                present_in_both = True
                break
            else:
                left += 1
                right -= 1
        if present_in_both is False:
            ans.append(array1[i])
	# find the elements present in array2 and not in array 1 excluding the common elements
    for i in range(0, n):
        present_in_both = False
        left = 0
        right = m - 1
        while left < right:

            if array2[i] == array1[left] or array2[i] == array1[right]:
                present_in_both = True
                break
            else:
                left += 1
                right -= 1

        if present_in_both is False:
            ans.append(array2[i])
	
    return (ans)


m = int(input())
array1 = list(map(int, input().rstrip().split()))
n = int(input())
array2 = list(map(int, input().rstrip().split()))
output = symmetric_diff(m, array1, n, array2)
output.sort()
for x in output:
    print(x)
    
"""

#with sets
def symmetric_diff(m, array1, n, array2):
	#symmetric difference of two sets A and B is (A-B) union (B-A)
    a = set(array1)- set(array2) 
    b = set(array2) - set(array1)

    return list(a.union(b))

m = int(input())
array1 = list(map(int, input().rstrip().split()))
n = int(input())
array2 = list(map(int, input().rstrip().split()))
output = symmetric_diff(m, array1, n, array2)
output.sort()
for x in range(0, len(output)):
  print(output[x])