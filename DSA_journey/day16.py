class node:
    def __init__(self,data):
        self.data=data
        self.next=None
# create nodes
a=node(10)
b=node(20)
c=node(30)
d=node(40)
e=node(50)
# connect nodes
a.next=b
b.next=c
c.next=d
d.next=e
head=a
slow=head
fast=head
while fast is not None and fast.next is not None:
    slow=slow.next
    fast=fast.next.next

print("middle node:",slow.data)
# middle node: 30


class Node: 
    def __init__(self,data):
        self.data=data
        self.next=None
n=int(input("enter no.of nodes:"))
head=None
tail=None
for i in range(n):
    data=int(input("enter node value:"))
    new_node=Node(data)
    if head is None:
        head=new_node
        tail=new_node
    else:
        tail.next=new_node
        tail=new_node
current=head
while current is not None:
    print(current.data,end="->")
    current=current.next
print("None")
# enter no.of nodes:4
# enter node value:10
# enter node value:20
# enter node value:30
# enter node value:40
# 10->20->30->40->None


# practice
class Node: 
    def __init__(self,data):
        self.data=data
        self.next=None
n=int(input("enter no.of nodes:"))
head=None
tail=None
for i in range(n):
    data=int(input("enter node value:"))
    new_node=Node(data)
    if head is None:
        head=new_node
        tail=new_node
    else:
        tail.next=new_node
        tail=new_node
current=head
slow=head
fast=head
while fast is not None and fast.next is not None:
    slow=slow.next
    fast=fast.next.next

print("middle node:",slow.data)
# Exercise 1 — Find the middle

# enter no.of nodes:5
# enter node value:5
# enter node value:15
# enter node value:25
# enter node value:35
# enter node value:45
# middle node: 25

# Exercise 2 — Even number of nodes

# enter no.of nodes:4
# enter node value:11
# enter node value:22
# enter node value:33
# enter node value:44
# middle node: 33

# Exercise 3 — Single node

# enter no.of nodes:1
# enter node value:100
# middle node: 100

# Exercise 4 — Empty list
class Node: 
    def __init__(self,data):
        self.data=data
        self.next=None
head = None
slow = head
fast = head

while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

if slow is None:
    print("The linked list is empty")
else:
    print("Middle node:", slow.data)

# The linked list is empty

# Exercise 5 — Trace the pointers

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create the linked list
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

head = a

# Initialize slow and fast pointers
slow = head
fast = head
iteration = 1

print("Initial: slow =", slow.data, ", fast =", fast.data)

# Trace the pointers
while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

    print("Iteration", iteration,
          ": slow =", slow.data,
          ", fast =", fast.data if fast else None)

    iteration += 1

# Print the middle node
if slow is None:
    print("The linked list is empty")
else:
    print("Middle node:", slow.data)
# Initial: slow = 1 , fast = 1
# Iteration 1 : slow = 2 , fast = 3
# Iteration 2 : slow = 3 , fast = 5
# Iteration 3 : slow = 4 , fast = 7
# Middle node: 4