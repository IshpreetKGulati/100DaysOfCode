"""
Function to check if a singly linked list is a palindrome
Given a singly linked list of characters, write a function that returns True if the given list is a palindrome, else False.

Sample input
("r" -> "a" -> "d" -> "a" -> "r" )

Sample output
True
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Linked_list: #to create a new list
    def __init__(self):
        # Createe an empty list
        self.tail = None
        self.head = None
        self.count = 0
    def append_item(self, val):
      node = ListNode(val)
      if self.head is None:       
        self.head = ListNode(val)
        self.count += 1
        return
      else:
        pre = self.head
        while(pre.next != None):
          pre = pre.next
        pre.next = node
        self.tail = node
        self.count += 1

    def print_list(self):
      c = 0
      n = self.head
      while (self.count != c):
        print(n.val)
        n = n.next
        c+=1
      
def rev(l1:ListNode): #to reverse the list
	# we need two pointers, the current node and the previous node, 
  head = l1
  prev = None
  cur = l1
  #update the previous and current node, set previous node equal to the cureent node and the current node to the next node after the current node
  #and current.next to the previous node.
  while(cur is not None):
  
    temp = cur.next
    cur.next = prev
    prev = cur
    cur = temp

  l1 = prev
 # print(l1)
  return(l1)      

class Solution:
    def checkPalindrome(self, l1: ListNode):
      palindrome = True
      h = l1
      temp_list = Linked_list()
      while(l1 is not None): #create a temporary list, and reverse it
        temp_list.append_item(l1.val)
        l1= l1.next
      s = rev(temp_list.head)
      
      while(s is not None):    
       
        if h.val != s.val: #if the reversed list is not equal to original list, set palindrome to false, else true
          palindrome = False
        s = s.next
        h = h.next
          
      return palindrome

