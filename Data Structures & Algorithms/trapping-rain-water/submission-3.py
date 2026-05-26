class Solution:
    def trap(self, height: List[int]) -> int:

        total_area = 0
        size = len(height)
        prefix = [0]
        suffix = [0]

        # left to right
        for i in range(size):
            prefix.append(max(height[i], prefix[-1]))

        for i in range(size - 1, 0, -1):
            suffix.append(max(height[i], suffix[-1]))

        suffix = suffix[::-1]
        for i, a in enumerate(height):
            area = 0
            if i == 0 or i == len(height) - 1:
                continue

            l = prefix[i]
            r = suffix[i]
            area = (min(l , r) - height[i])
            if area < 0:
                area = 0
            total_area += area

            
        return total_area


