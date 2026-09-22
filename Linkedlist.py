class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class linkedlist:
  def __init__(self):
    self.head=None
    self.size=0
  def add(self,data):
    if self.head==None:
      self.head=Node(data)
      self.size+=1
      return
    cn=self.head
    while cn.next is not None:
      cn=cn.next
    cn.next=Node(data)
    self.size+=1
  def traversal(self):
    if self.head==None:
        print('no elements')
    cn=self.head
    while cn is not None:
        print(cn.data,end="->")
        cn=cn.next
    print(cn)
  def search(self,data):

    cn=self.head
    ind=0
    while cn is not None:
        if cn.data == data:
          print(f'element {data} is at {ind} index')
          return
        cn=cn.next
        ind+=1
    print('element not found')
  def length(self):
    return self.size
  def insBig(self,data):
    obj=Node(data)
    obj.next=self.head
    self.head=obj
  def delbig(self):
    if self.head is None:
        return
    self.head=self.head.next


ll=linkedlist()
ll.add(10)
ll.add(20)
ll.add(30)
ll.traversal()
ll.search(20)
print(ll.length())
ll.insBig(5)
ll.traversal() 
ll.delbig()  
ll.traversal()




class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class Linkedlist:
  def __init__(self):
    self.head=None
  def add(self,data):
    obj=Node(data)
    if self.head==None:
      self.head=obj
      return
    cn=self.head
    while cn.next is not None:
      cn=cn.next
    cn.next=obj
  def traverse(self):
    cn=self.head
    while cn.next is not None:
      print(cn.data,end="->")
      cn=cn.next
    print(cn.data)
  def delfirst(self):
    self.head=self.head.next
  def dellast(self):
    # self.head.next.next=None
    cn=self.head
    if cn.next is None:
      cn=None
    while cn.next.next is not None:
      cn=cn.next
    cn.next=None
  def insAt(self,data,position):
    node1=Node(data)
    if position == 0:
      node1.next = self.head
      self.head =node1
      return
  
    current = self.head
    for i in range(position - 1):
      if current is None:
          return
      current = current.next
  
    if current is None:
      return 
    node1.next = current.next
    current.next =node1
  def delAt(self,position):
    if self.head is None:
      return None
  
    if position == 0:
      d = self.head.data
      self.head = self.head.next
      return d
    current = self.head
    for i in range(position-1):
      if current.next is None:
          return None  
      current = current.next
    d= current.next.data
    current.next = current.next.next
    return d
  
  def insfirst(self,data,position):
    node2=Node(data)
    if position==0:
      node2.next = self.head
      self.head =node2
      return
  def delbyvalue(self,target):
    if self.head is None:
      return False
    if self.head.data==target:
      self.head=self.head.next
      return True
    current=self.head
    while current.next is not None:
      if current.next.data==target:
        current.next=current.next.next
        return True
      current=current.next
    return False
  def count(self,data):
    if self.head is None:
      return 0
    c=0
    cn=self.head
    while cn.next is not None:
      if cn.data==data:
        c+=1
      cn=cn.next
    if cn.data==data:
      c+=1
    return c


    



ll=Linkedlist()
ll.add(10)
ll.add(20)
ll.add(30)
ll.add(40)
ll.add(50)
ll.traverse()
ll.delfirst()
ll.traverse()
ll.dellast()
ll.traverse()
ll.insAt(60,2)
ll.traverse()
ll.delAt(3)
ll.traverse()
ll.insfirst(70,0)
ll.traverse()
ll.delbyvalue(20)
ll.traverse()
ll.add(70)
ll.traverse()
print(ll.count(70))
