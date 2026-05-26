class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        prefix = [1]
        suffix = [1]

        for i in range(1, len(nums)):
            prefix.append(prefix[-1] * nums[i - 1])

        for i in range(len(nums), 1, -1):
            suffix.append(suffix[-1] * nums[i - 1])


        suffix = suffix[::-1]
        for i in range(len(nums)):
            ans.append(prefix[i] * suffix[i])

        return ans
            

        
        