class Solution:
    def trap(self, height: List[int]) -> int:

        total_area = 0
        for i, a in enumerate(height):
            area = 0
            if i == 0 or i == len(height) - 1:
                continue


            l = max(height[0 : i])
            r = max(height[i + 1 :])
            area = (min(l , r) - height[i])
            if area < 0:
                area = 0
            total_area += area

            
        return total_area


