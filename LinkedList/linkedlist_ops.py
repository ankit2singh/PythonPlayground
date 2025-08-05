class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self,val): # TC -> O(n), SC -> O(1)
        new_node = Node(val)
        # self.head = None 

        if self.head is None:
            self.head = new_node

        else:
            curr = self.head
            while curr.next is not None: # last node have "None" address
                curr = curr.next
            
            curr.next = new_node    

    def traversal(self): # TC-n, Sc-1
        if self.head is None:
            print("SLL is empty")
        else:
            curr = self.head

            while curr is not None:
                print(curr.val, end= " ")

                curr = curr.next    
            # print()
    
    def insert_at(self, val, position): # TC-n, Sc-1
        new_node = Node(val)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            prev_node = None
            count = 0    

            while curr.next is not None and count < position:

                prev_node = curr

                curr = curr.next

                count += 1

            prev_node.next = new_node

            new_node.next = curr

    def delete(self, val):
        temp = self.head
        if temp.next is not None:

            if temp.val == val:
                self.head = temp.next
                # del temp (optional)
                return
            else:
                found = False
                prev = None

                while temp is not None:
                    
                    if temp.val == val:

                        found = True

                        break

                    prev = temp

                    temp = temp.next

                if found:
                    prev.next = temp.next
                    return
                else:
                    print("element not found")        



sll = SinglyLinkedList()

sll.append(4)
sll.append(433)
sll.append(64)
sll.append(684)
sll.append(43)
sll.append(423)
sll.append(614)
sll.append(6084)

sll.traversal()
sll.delete(6084)
sll.traversal()