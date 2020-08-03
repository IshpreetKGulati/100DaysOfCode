"""
Given a linked list, remove the n-th node from the end of the list and return its head.
Example:
Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
"""
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
      self.c = 0 # number of nodes
      node = head
      
      #find the number of nodes
      while (node is not None):
        self.c += 1
        node = node.next
      
      # convert n from last to n from start  
      n = self.c - n + 1
      cur = head
      self.prev = None
      i = 1
      #find the nth node
      while (i != n):
        self.prev = cur
        cur = cur.next
        i += 1

      # delete the first element  
      if n == 1:
        head = head.next
      
      #else set the next of previous to the next of the current node which is the nth node 
      else:
        self.prev.next = cur.next  
  
      return head
        
      
      
        

    
    


    
    
    
    
    
