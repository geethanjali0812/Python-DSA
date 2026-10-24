
# Day 17: Linked List Cycle Detection
# Algorithm: Floyd's Cycle Detection (Slow and Fast Pointers)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def has_cycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False


# Example 1: Cycle connects back to node 2
a = Node(3)
b = Node(2)
c = Node(0)
d = Node(-4)

a.next = b
b.next = c
c.next = d
d.next = b

head = a
print("Example 1:", has_cycle(head))  # True


# Example 2: Cycle connects back to the first node
e = Node(1)
f = Node(2)

e.next = f
f.next = e

head = e
print("Example 2:", has_cycle(head))  # True


# Example 3: Single node, no cycle
g = Node(1)
head = g

print("Example 3:", has_cycle(head))  # False


# Example 4: Normal linked list, no cycle
h = Node(10)
i = Node(20)
j = Node(30)

h.next = i
i.next = j

head = h
print("Example 4:", has_cycle(head))  # False


# Example 5: Empty linked list
head = None
print("Example 5:", has_cycle(head))  # False



# Outputs

# Example 2: True
# Example 3: False
# Example 4: False
# Example 5: False