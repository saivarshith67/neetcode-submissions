class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (nums == []):
            return 0

        sorted_nums = sorted(set(nums))
        op = 1
        max_op = -1
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] - sorted_nums[i - 1] == 1:
                op += 1
            else:
                max_op = max(max_op, op)
                op = 1

        return max(max_op, op)