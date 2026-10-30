
# Day 20: Remove Nth Node From End of Linked List
# Topic: Linked Lists
# Technique: Two Pointers + Dummy Node
# LeetCode: 19
# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Function to create a linked list
def create_linked_list(values):
    if not values:
        return None

    head = Node(values[0])
    current = head

    for value in values[1:]:
        current.next = Node(value)
        current = current.next

    return head


# Function to print a linked list
def print_linked_list(head):
    current = head

    while current is not None:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


# Function to remove the Nth node from the end
def remove_nth_from_end(head, n):

    # Create a dummy node
    dummy = Node(0)
    dummy.next = head

    # Initialize fast and slow pointers
    fast = dummy
    slow = dummy

    # Move fast pointer ahead by n nodes
    for _ in range(n):
        if fast.next is None:
            return head
        fast = fast.next

    # Move both pointers until fast reaches the last node
    while fast.next is not None:
        fast = fast.next
        slow = slow.next

    # Remove the target node
    slow.next = slow.next.next

    # Return the updated head
    return dummy.next


# Example 1: Remove the 2nd node from the end

print("Example 1: Remove 2nd node from end")

head = create_linked_list([10, 20, 30, 40, 50])

print("Original list:")
print_linked_list(head)

head = remove_nth_from_end(head, 2)

print("Updated list:")
print_linked_list(head)


# Example 2: Remove the last node

print("\nExample 2: Remove last node")

head = create_linked_list([1, 2, 3, 4])

head = remove_nth_from_end(head, 1)

print_linked_list(head)


# Example 3: Remove the first node

print("\nExample 3: Remove first node")

head = create_linked_list([5, 10, 15, 20])

head = remove_nth_from_end(head, 4)

print_linked_list(head)


# Example 4: Single-node linked list

print("\nExample 4: Single-node list")

head = create_linked_list([100])

head = remove_nth_from_end(head, 1)

print_linked_list(head)


# Example 5: Empty linked list

print("\nExample 5: Empty list")

head = None

head = remove_nth_from_end(head, 1)

print_linked_list(head)


# Output
# Example 1: Remove 2nd node from end
# Original list:
# 10 -> 20 -> 30 -> 40 -> 50 -> None
# Updated list:
# 10 -> 20 -> 30 -> 50 -> None

# Example 2: Remove last node
# 1 -> 2 -> 3 -> None

# Example 3: Remove first node
# 10 -> 15 -> 20 -> None

# Example 4: Single-node list
# None

# Example 5: Empty list
# None