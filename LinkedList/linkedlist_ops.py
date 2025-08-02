class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self,val):
        new_node = Node(val)
        # self.head = None 

        if self.head is None:
            self.head = new_node

        else:
            curr = self.head
            while curr.next is not None: # last node have "None" address
                curr = curr.next
            
            curr.next = new_node    

    def traversal(self):
        if self.head is None:
            print("SLL is empty")
        else:
            curr = self.head

            while curr is not None:
                print(curr.val, end= " ")

                curr = curr.next    
            # print()
    
    def insert()

sll = SinglyLinkedList()

sll.append(4)
sll.append(43)
sll.append(64)
sll.append(684)

sll.traversal()