class Solution:
    @staticmethod
    def find_pivot_index(nums: List[int], n : int) -> int:
        l,r = 0, n-1
        while l <= r:
            mid = (l + r) // 2
            if mid + 1 < n and nums[mid] > nums[mid + 1]:
                return mid
            if mid - 1 >= 0 and nums[mid] < nums[mid - 1]:
                return mid - 1
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return n - 1

    @staticmethod
    def binary_search(nums: List[int], l : int, r : int, target : int) -> int:
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1

            
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pivot_index = self.find_pivot_index(nums, n)
        idx1 = self.binary_search(nums, 0, pivot_index, target)
        idx2 = self.binary_search(nums, pivot_index + 1, n-1, target)

        if idx1 != -1:
            return idx1
        if idx2 != -1:
            return idx2

        return -1