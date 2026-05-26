class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]
        right_prod = 1

        for i in range(1, len(nums)):
            ans.append(ans[-1] * nums[i - 1])

        for i in range(len(nums), 1, -1):
            # suffix.append(suffix[-1] * nums[i - 1])
            ans[i - 1] *= right_prod
            right_prod *= nums[i - 1]

        ans[0] = right_prod
        return ans
            

        
        