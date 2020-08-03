"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.
For example, given the following linked lists :
5 -> 8 -> 20 
4 -> 11 -> 15
The merged list should be :
4 -> 5 -> 8 -> 11 -> 15 -> 20
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

class Solution:
    def addTwoLinkedLists(self, l1: ListNode, l2: ListNode) -> ListNode:
      self.n1 = 0 #number of nodes in list 1
      self.n2 = 0 #number of nodes in list2
      
      h1 = l1 #head of list1
      h2 = l2 #head of list2
      ans = Linked_list()
      
      #find the number of nodes in l1
      while (h1 is not None):
        h1 = h1.next
        self.n1 += 1

      #find the number of nodes in l1
      while (h2 is not None):
        h2 = h2.next
        self.n2 += 1
      i = j = 0

      #find the smaller node of both the lists and append it to the answer list
      while l1 is not None and l2 is not None:
        if l1.val < l2.val:
          ans.append_item(l1.val)
          l1 = l1.next
          i += 1
        else:
          ans.append_item(l2.val)
          l2 = l2.next
          j += 1

      #append all left out nodes from the list1
      while i != self.n1:
        ans.append_item(l1.val)
        l1 = l1.next
        i += 1

      #append all left out nodes from the list1
      while j != self.n2:
        ans.append_item(l2.val)
        l2 = l2.next
        j += 1

      return (ans.head)



l1 = [2, 3, 7]
l2 = [4, 5, 6]
    
ll1 = Linked_list() 
ll2 = Linked_list()

for i in range(0, len(l1)):
  ll1.append_item(l1[i])
    
for i in range(0, len(l2)):
  ll2.append_item(l2[i])

s = Solution()
x = s.addTwoLinkedLists(ll1.head, ll2.head)
while x is not None:
  print(x.val)
  x = x.next
