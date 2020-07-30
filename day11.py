"""
Write a Python program to search a specific item in a singly linked list and return true if the item is found otherwise return false.
Sample input
items = singly_linked_list()
items.append_item('PHP')
items.append_item('Python')
items.append_item('C#')
items.append_item('C++')
items.append_item('Java')
items.search_item('SQL')

Sample output
False
"""

class Node:
    # Singly linked node
    def __init__(self, data=None):
        self.data = data
        self.next = None
class singly_linked_list:
    def __init__(self):
        # Createe an empty list
        self.tail = None
        self.head = None
        self.count = 0
    def append_item(self, data):
      #add the new item
      self.node = Node(data)
      if self.head is None: #if the list is empty      
        self.head = self.node
        self.count += 1
        return
 
      else: #if the list has some element, then move to the end and then append the element
        self.pre = self.head
        while(pre.next != None):
          self.pre = self.pre.next
        self.pre.next = self.node
        self.tail = self.node
        self.count += 1
        
        
    def print_list(self):
    	#to pribbt the list
      self.n = self.head
      while (self.n != None):
        print(self.n.data)
        self.n = self.n.next

      print(self.count)
        
    def search_item(self, val):
        self.Found = False
        self.c = 0
        # Search the list
        self.pre = self.head
        while (self.c < self.count):
          if self.pre.data == val:
           self.Found = True
          else:
             self.pre  = self.pre.next
          self.c += 1

        if self.Found is not True:
          return False
        else:
          return True

if __name__ == "__main__":
  items = singly_linked_list()
  items.append_item('PHP')
  items.append_item('Python')
  items.append_item('C#')
  items.append_item('C++')
  items.append_item('Java')
  
  print(items.search_item('SQL'))