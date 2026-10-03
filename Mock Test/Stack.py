# implement queue using a stack
# class of the stack

class Stack:
    def __init__(self):
        self.values = []
        self.head = -1

    def add(self, value):
        self.values.append(value)
        self.head += 1

    def delete(self):
        val = self.values.pop()
        self.head -= 1
        return val


class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def insert(self, value):
        self.stack1.add(value)

    def delete(self):
        while self.stack1.values:
            val = self.stack1.delete()
            self.stack2.add(val)

        val = self.stack2.delete()

        while self.stack2.values:
            x = self.stack2.delete()
            self.stack1.add(x)

        return val


q = Queue()

q.insert(10)
q.insert(20)
q.insert(30)

print("Deleted:", q.delete())
print("Deleted:", q.delete())