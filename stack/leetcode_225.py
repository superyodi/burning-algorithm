
# 225. Implement Stack using Queues

# [Try 1: Accepted]	24 ms	14.4 MB

import collections

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # push
        self.q1 = collections.deque()
        # pop
        self.q2 = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """

        # 여기서 큐 -> 스택 정렬
        if not self.q1:
            # q1가 비었을때
            self.q1.append(x)

            while self.q2:
                self.q1.append(self.q2.popleft())


        else:
            # q2가 비었을때
            self.q2.append(x)

            while self.q1:
                self.q2.append(self.q1.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.q1:
            return self.q1.popleft()
        else:
            return self.q2.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.q1:
            return self.q1[0]
        else:
            return self.q2[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if not self.q1 and not self.q2:
            return True
        return False