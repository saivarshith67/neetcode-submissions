# structure
# (val, min)
class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        tup = None
        if not self.st:
            tup = (val, val)
        else:
            min_element = min(self.getMin(), val)
            tup = (val, min_element)
        self.st.append(tup)

        

    def pop(self) -> None:
        self.st.pop()
        

    def top(self) -> int:
        element, min_element = self.st[-1]
        return element
        

    def getMin(self) -> int:
        element, min_element = self.st[-1]
        return min_element
