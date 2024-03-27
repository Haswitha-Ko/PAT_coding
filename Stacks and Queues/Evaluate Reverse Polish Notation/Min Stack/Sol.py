class MinStack:

    def __init__(self):
        self.ms=[]
        self.mains=[]

    def push(self, val: int) -> None:
        self.mains.append(val)
        if not self.ms or val<=self.ms[-1]:
            self.ms.append(val)

    def pop(self) -> None:
        popped=self.mains.pop()
        if popped==self.ms[-1]:
            self.ms.pop()

    def top(self) -> int:
        return self.mains[-1]


    def getMin(self) -> int:
        return self.ms[-1]
