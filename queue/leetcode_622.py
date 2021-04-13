# 622. Design Circular Queue (원형 큐 구현)

# [Try1. Accepted]	64 ms	14.9 MB
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1] * k
        self.front = 0
        self.rear = 0
        self.size = k

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        s = self.size
        return self.front % s == self.rear % s and self.front != self.rear

    def enQueue(self, value: int) -> bool:

        if self.isFull():
            return False

        self.queue[self.rear % self.size] = value
        self.rear += 1

        # print(self.queue)
        return True

    def deQueue(self) -> bool:

        if self.isEmpty():
            # print("empty", self.queue)
            return False

        self.queue[self.front % self.size] = -1
        self.front += 1
        return True

    def Front(self) -> int:
        return self.queue[self.front % self.size]

    def Rear(self) -> int:

        return self.queue[(self.rear - 1) % self.size]

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()