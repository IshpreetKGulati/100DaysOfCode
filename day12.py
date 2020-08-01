"""
Instructions from your teacher:
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Sample input
(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)

Sample output
7 -> 8 -> 0 -> 7

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Linked_list:
    def __init__(self):
        # Createe an empty list
        self.tail = None
        self.head = None
        self.count = 0
    def append_item(self, val):
      self.node = ListNode(val)

      if self.head is None:       
        self.head = node
        self.count += 1
        return
 
      else:
        self.pre = self.head
        while(pre.next != None):
          pre = pre.next

        self.pre.next = self.node
        self.tail = self.node
        self.count += 1
      
class Solution:
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
      self.n1 = 1
      self.n2 = 1
      self.s1 = self.s2 =""
      while(l1 is not None):
        self.n1 += 1
        self.s1+= str(l1.val)
        l1 = l1.next
  
      while(l2 is not None):
        self.n2 += 1
        self.s2 += str(l2.val)
        l2 = l2.next
        
      self.s = str(int(s1) + int(s2))
      self.ans = Linked_list()
      for i in range(0, len(self.s)):
         self.ans.append_item(int(self.s[i]))
         
      return self.ans.head
      

    
    
    
    
    
