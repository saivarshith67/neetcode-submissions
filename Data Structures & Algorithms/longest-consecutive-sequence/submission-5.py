class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if (nums == []):
        #     return 0

        # sorted_nums = sorted(set(nums))
        # op = 1
        # max_op = -1
        # for i in range(1, len(sorted_nums)):
        #     if sorted_nums[i] - sorted_nums[i - 1] == 1:
        #         op += 1
        #     else:
        #         max_op = max(max_op, op)
        #         op = 1

        # return max(max_op, op)

        """
        if left neighbour doesn't exist in the set => start of the sequence
        if left neigbhour exist in the set => not start of the sequence => skip
        if right neighbour exist in the set => continue checking for it's right neighbout in the set
        """

        hash_set = set(nums)
        longest = 0
        for num in nums:
            # start of sequence
            if num - 1 not in hash_set:

                length = 0

                while (num + length) in hash_set:
                    length += 1

                longest = max(longest, length)


        return longest

    