class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2

            # If mid element is greater than rightmost element,
            # the min must be to the right of mid
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                # Min is at mid or to the left
                r = mid
        
        # When l == r, we have found the minimum
        return nums[l]
