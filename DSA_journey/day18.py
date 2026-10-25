
# Day 18: Reverse a Linked List
# Technique: Three Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_linked_list(head):
    prev = None
    current = head

    while current is not None:
        # Step 1: Save the next node
        temp = current.next

        # Step 2: Reverse the current link
        current.next = prev

        # Step 3: Move prev forward
        prev = current

        # Step 4: Move current forward
        current = temp

    # prev is the new head
    return prev


def print_linked_list(head):
    current = head

    while current is not None:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


# Example 1: Multiple nodes
a = Node(10)
b = Node(20)
c = Node(30)

a.next = b
b.next = c

head = a

print("Original list:")
print_linked_list(head)
# 10 -> 20 -> 30 -> None

head = reverse_linked_list(head)

print("Reversed list:")
print_linked_list(head)
# 30 -> 20 -> 10 -> None


# Example 2: Single node
s = Node(5)
s = reverse_linked_list(s)

print("Single-node list:")
print_linked_list(s)
# 5 -> None


# Example 3: Empty list
empty = None
empty = reverse_linked_list(empty)

print("Empty list:")
print_linked_list(empty)
# None


# practice 1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_linked_list(head):
    prev = None
    current = head

    while current is not None:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev


def print_linked_list(head):
    current = head

    while current is not None:
        print(current.data, end=" -> ")
        current = current.next

    print("None")
a=Node(5)
b=Node(10)
c=Node(15)
a.next=b
b.next=c
head= a
head = reverse_linked_list(head)

print("Reversed list:")
print_linked_list(head)   #15 -> 10 -> 5 -> None




