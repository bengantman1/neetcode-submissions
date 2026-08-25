class MinStack:

    def __init__(self):
        self.stack = []
        self.pref = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.pref or self.pref[-1] > val:
            self.pref.append(val)
        else:
            self.pref.append(self.pref[-1])

    def pop(self) -> None:
        self.pref.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.pref[-1]
