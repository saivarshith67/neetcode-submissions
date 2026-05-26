class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        prod = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                prod *= nums[j]

            ans.append(prod)
            prod = 1

        return ans

        
        