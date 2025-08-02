class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


N1 = Node(5)
N2 = Node(50)
N3 = Node(500)

N1.next = N2
N2.next = N3

print(N1.val, N2.val, N3.val)