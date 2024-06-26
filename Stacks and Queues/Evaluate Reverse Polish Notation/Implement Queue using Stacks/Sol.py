class MyQueue:

    def __init__(self):
        self.q=[]

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        return self.q.pop(0)

    def peek(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        if len(self.q)==0:
            return True
        else:
            return False
