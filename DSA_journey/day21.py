
# Day 21: Palindrome Linked List
# Topic: Linked Lists
# Technique: Slow and Fast Pointers + Reversing a Linked List
# LeetCode: 234
# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def create_linked_list(values):
    """Create a linked list from a Python list."""
    if not values:
        return None

    head = Node(values[0])
    current = head

    for value in values[1:]:
        current.next = Node(value)
        current = current.next

    return head


def print_linked_list(head):
    """Print all nodes in the linked list."""
    current = head

    while current is not None:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


def reverse_linked_list(head):
    """Reverse a linked list and return its new head."""
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


def is_palindrome(head):
    """Check whether a linked list is a palindrome."""

    # An empty list or a single-node list is a palindrome.
    if head is None or head.next is None:
        return True

    # Step 1: Find the middle using slow and fast pointers.
    slow = head
    fast = head

    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half.
    second_half = reverse_linked_list(slow.next)

    # Step 3: Compare the first and second halves.
    first_half = head
    second_half_copy = second_half
    result = True

    while second_half_copy is not None:
        if first_half.data != second_half_copy.data:
            result = False
            break

        first_half = first_half.next
        second_half_copy = second_half_copy.next

    # Step 4: Restore the original linked list.
    slow.next = reverse_linked_list(second_half)

    return result


# -------------------------------
# TEST CASES
# -------------------------------

# Example 1: Even-length palindrome
print("Example 1: Even-length palindrome")
head = create_linked_list([1, 2, 2, 1])
print("Linked list:")
print_linked_list(head)
print("Is palindrome?", is_palindrome(head))
print("After checking:")
print_linked_list(head)

# Example 2: Odd-length palindrome
print("\nExample 2: Odd-length palindrome")
head = create_linked_list([1, 2, 3, 2, 1])
print("Linked list:")
print_linked_list(head)
print("Is palindrome?", is_palindrome(head))

# Example 3: Not a palindrome
print("\nExample 3: Not a palindrome")
head = create_linked_list([1, 2, 3, 4])
print("Linked list:")
print_linked_list(head)
print("Is palindrome?", is_palindrome(head))

# Example 4: Single-node list
print("\nExample 4: Single-node list")
head = create_linked_list([5])
print("Is palindrome?", is_palindrome(head))

# Example 5: Empty list
print("\nExample 5: Empty list")
head = None
print("Is palindrome?", is_palindrome(head))

# Example 6: Two different nodes
print("\nExample 6: Two different nodes")
head = create_linked_list([1, 2])
print("Is palindrome?", is_palindrome(head))

# Output

# Example 1: Even-length palindrome
# Linked list:
# 1 -> 2 -> 2 -> 1 -> None
# Is palindrome? True
# After checking:
# 1 -> 2 -> 2 -> 1 -> None

# Example 2: Odd-length palindrome
# Linked list:
# 1 -> 2 -> 3 -> 2 -> 1 -> None
# Is palindrome? True

# Example 3: Not a palindrome
# Linked list:
# 1 -> 2 -> 3 -> 4 -> None
# Is palindrome? False

# Example 4: Single-node list
# Is palindrome? True

# Example 5: Empty list
# Is palindrome? True

# Example 6: Two different nodes
# Is palindrome? False