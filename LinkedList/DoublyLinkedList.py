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
       
    def append(self, val):
       new_node = Node(val)
       
       if not self.head:
          head = new_node
       else:
          curr = self.head
          while curr.next:
             curr = curr.next
          curr.next = new_node
          new_node.prev = curr


     def inser_at_position(val, position):
           new_node = Node(val)
           if position == 0:
              return insert_at_head(val)
           curr = self.head
           count = 0 
           while curr.next and count < position - 1:
              curr = curr.next
              count += 1
           new_node.next = curr.next
           new_node.prev = curr

           if curr.next:
              curr.next.prev = new_node
           curr.next = new_node   
           
          
