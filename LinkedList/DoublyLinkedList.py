class Node:
   def __init__(self, val):
      self.val = val
      self.next = None
      self.next = None

 class DoublyLinkedList:

    def __init__(self):
       self.head = None
   
    def insert_at_head(self, val):
       new_node = self.val
       if not self.head:
         self.head = new_node
       else:  
         new_node.next = head
         head.prev = new_node
         head = new_node
       
    
