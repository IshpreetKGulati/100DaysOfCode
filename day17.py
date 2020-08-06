"""
Given a singly linked list and an integer K, reverses the nodes of the
list K at a time and returns modified linked list.
NOTE : The length of the list is divisible by K
Example :
Given linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 and K=2,
You should return 2 -> 1 -> 4 -> 3 -> 6 -> 5
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
       
class Solution:
    def swapLinkedLists(self, l1: ListNode,key: int) -> ListNode:
    	#prev points to the previous node
    	#cur points to the current node
    	#temp points to the next node
        
        head = l1
        prev = None
        cur = l1
        #reverse the linked list
        if cur.next is not None:
            for i in range(0, key):
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
                
        else:

                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
        # recursivly call the list function until the temp node is none
        if temp is not None:
           l1.next =  self.swapLinkedLists(temp,key)
        l1 = prev
        return (l1)
        
        