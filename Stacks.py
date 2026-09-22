class Stack:
    def __init__(self):
        self._ar = []
        self._top = None

    def push(self, data):
        if self._top is None:
            self._top = 0
            self._ar.append(data)
        else:
            self._top += 1
            self._ar.append(data)

    def peek(self):
        if self._top is None:
            print("Stack is empty")
        else:
            print( self._ar[self._top])
    def is_empty(self):
        return self._top is None
    def pop(self):
        if self._top is None:
            print("Stack is empty")
        else:
            data = self._ar.pop()
            self._top -= 1

            if self._top < 0:
                self._top = None

            return data

s = Stack()
s.push(10)
s.push(20)
s.push(30)

s.peek()
print(s.is_empty())
print(s.pop())