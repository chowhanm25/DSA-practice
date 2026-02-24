from collections import deque

class MyStack(object):

    def __init__(self):
        self.q1 = deque()  # main queue
        self.q2 = deque()  # temporary queue

    def push(self, x):
        # Always push into q1
        self.q1.append(x)

    def pop(self):
        # Move all but the last element from q1 to q2
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        
        # Last element is the stack top
        top_element = self.q1.popleft()

        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1

        return top_element

    def top(self):
        # Move all but the last element from q1 to q2
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        
        # Peek the last element
        top_element = self.q1.popleft()
        self.q2.append(top_element)  # put it back after peeking

        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1

        return top_element

    def empty(self):
        return len(self.q1) == 0
