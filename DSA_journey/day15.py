# Linked list Basics
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
# create nodes
first=node(10)
second=node(20)
third=node(30)
# connect nodes
first.next=second
second.next=third
head=first
current=head
print("Linked List:")
while current is not None:
    print(current.data,end="->")
    current=current.next
print("None")

# output
# Linked List:
# 10->20->30->None

# practice problems
# problem 1
# Create nodes containing 5, 15, and 25. Connect them and print every value.
# Hint: Start with head, then use current and a while loop.
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=node(5)
b=node(15)
c=node(25)
a.next=b
b.next=c
head=a
current=head
while current is not None:
    print(current.data,end="->")
    current=current.next
print("None")

# 5->15->25->None

# problem 2
# For the list 10 → 20 → 30 → 40, count and print the total number of nodes.
# Hint: Initialize count = 0. Increase it each time you visit a node.
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.count=count
count=0
a=node(10)
b=node(20)
c=node(30)
d=node(40)
a.next=b
b.next=c
c.next=d
head=a
current=head
while current is not None:
    print(current.data,end="->")
    count+=1
    current=current.next
    
    
    
print("None")
print("Total nodes:",count)
# 10->20->30->40->None
# Total nodes: 4

# problem 3
# Search for 30 in 10 → 20 → 30 → 40. Print Found if it exists; otherwise print Not found.
# Hint: Compare current.data with the target at each step.
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        

a=node(10)
b=node(20)
c=node(30)
d=node(40)

a.next=b
b.next=c
c.next=d
head=a
current=head
key=30
found=False
while current is not None:
    if current.data==key:
        print("found")
        found=True
        break
    current=current.next
if not found:
    print("not found")
# found

# problem 4
# Find the sum of all node values in 5 → 10 → 15 → 20.
# Hint: Initialize total = 0 and add each node's data.
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=node(5)
b=node(10)
c=node(15)
d=node(20)

a.next=b
b.next=c
c.next=d
head=a
current=head
total=0
while current is not None:
    total+=current.data
    current=current.next
print("Sum:",total)
# Sum: 50

# problem 5
# Find the largest value in 12 → 7 → 35 → 18 → 24.
# Hint: Initialize maximum with the first node's value, then compare the remaining nodes.
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=node(12)
b=node(7)
c=node(35)
d=node(18)
e=node(24)

a.next=b
b.next=c
c.next=d
head=a
current=head
maxi=current.data
while current is not None:
    if maxi<current.data:
        maxi=current.data
    current=current.next
print("Maximum:",maxi)
# Maximum: 35   