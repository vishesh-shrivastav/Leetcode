class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

    def push(self, x: int) -> None:
        cur_min = self.getMin()
        if cur_min == None or x < cur_min:
            cur_min = x
        self.arr.append((x, cur_min))

    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        if len(self.arr) == 0:
            return None
        else:
            return self.arr[-1][0]

    def getMin(self) -> int:
        if len(self.arr) == 0:
            return None
        else:
            return self.arr[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
