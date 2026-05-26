class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        IDEA: the idea being if we sorted everything in increasing order of 
        position we can find the time taken by each car to reach the target.
        and we traverse it in reverse order so that we can get to know the
        formation of collisions easily. if time of current element is 
        greater than the top of stack 
        """

        pair = [[p,s] for p,s in zip(position, speed)]
        stack = []
        for p,s in sorted(pair)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
        