# Implement the class Queue using stacks. The queue methods you need to implement are enqueue, dequeue, peek, and empty

class Queue:
    def __init__(self):
        self.stack = []
        self.reverse_stack = []

    def enqueue(self, value):
        self.stack.append(value)

    def modify_stack(self):
        while len(self.stack) > 0:
            temp = self.stack.pop()
            self.reverse_stack.append(temp)

    def dequeue(self):
        # If reversed stack has items pop them.
        if len(self.reverse_stack) > 0:
            val = self.reverse_stack.pop()

        # If the reversed stack is empty, and there are items in the stack, pop the values into the reversed stack
        elif len(self.reverse_stack) == 0 and len(self.stack) > 0:
            self.modify_stack()
            val = self.reverse_stack.pop()

        else:
            val = -1
        return val

    def peek(self):
        if len(self.reverse_stack) > 0:
            val = self.reverse_stack[len(self.reverse_stack) - 1]


        elif len(self.reverse_stack) == 0 and len(self.stack) > 0:
            self.modify_stack()
            val = self.reverse_stack[len(self.reverse_stack) - 1]

        else:
            val = -1
        return val

    def empty(self):
        self.stack = []
        self.reverse_stack = []

    def print(self):
        print(f"Stack: {self.stack}")
        print(f"Reversed Stack: {self.reverse_stack}")


__name__ = "__main__"

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue.peek())
queue.empty()
queue.print()
