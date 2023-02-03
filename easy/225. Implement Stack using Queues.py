class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        self.queue1.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.pop(0))


    def pop(self) -> int:
        return self.queue2.pop()
    def top(self) -> int:
        return self.queue2[-1]
    def empty(self) -> bool:
        return len(self.queue2) == 0

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()