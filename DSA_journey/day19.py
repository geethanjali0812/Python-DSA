
# Day 19: Merge Two Sorted Linked Lists
# Topic: Linked Lists
# Technique: Two Pointers + Dummy Node
# LeetCode: 21 - Merge Two Sorted Lists
# Time Complexity: O(n + m)
# Auxiliary Space: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Function to merge two sorted linked lists
def merge_two_lists(list1, list2):

    # Create a dummy node
    dummy = Node(0)
    tail = dummy

    # Compare nodes from both lists
    while list1 is not None and list2 is not None:

        if list1.data <= list2.data:
            tail.next = list1
            list1 = list1.next

        else:
            tail.next = list2
            list2 = list2.next

        # Move tail forward
        tail = tail.next

    # Attach the remaining nodes
    if list1 is not None:
        tail.next = list1
    else:
        tail.next = list2

    # Return the merged list
    return dummy.next


# Function to display a linked list
def print_linked_list(head):

    current = head

    while current is not None:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


# Example 1: Two sorted linked lists

a = Node(1)
b = Node(3)
c = Node(5)

a.next = b
b.next = c

d = Node(2)
e = Node(4)
f = Node(6)

d.next = e
e.next = f

list1 = a
list2 = d

print("Example 1: Normal Lists")
print("First List:")
print_linked_list(list1)

print("Second List:")
print_linked_list(list2)

merged = merge_two_lists(list1, list2)

print("Merged List:")
print_linked_list(merged)


# Example 2: First list is empty

x = Node(2)
y = Node(4)

x.next = y

list1 = None
list2 = x

merged = merge_two_lists(list1, list2)

print("\nExample 2: First List Empty")
print_linked_list(merged)


# Example 3: Second list is empty

p = Node(1)
q = Node(3)

p.next = q

list1 = p
list2 = None

merged = merge_two_lists(list1, list2)

print("\nExample 3: Second List Empty")
print_linked_list(merged)


# Example 4: Both lists are empty

merged = merge_two_lists(None, None)

print("\nExample 4: Both Lists Empty")
print_linked_list(merged)


# Example 5: Duplicate values

m1 = Node(1)
m2 = Node(3)
m1.next = m2

n1 = Node(1)
n2 = Node(3)
n1.next = n2

merged = merge_two_lists(m1, n1)

print("\nExample 5: Duplicate Values")
print_linked_list(merged)

# Output
# Example 1: Normal Lists
# First List:
# 1 -> 3 -> 5 -> None
# Second List:
# 2 -> 4 -> 6 -> None
# Merged List:
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None

# Example 2: First List Empty
# 2 -> 4 -> None

# Example 3: Second List Empty
# 1 -> 3 -> None

# Example 4: Both Lists Empty
# None

# Example 5: Duplicate Values
# 1 -> 1 -> 3 -> 3 -> None