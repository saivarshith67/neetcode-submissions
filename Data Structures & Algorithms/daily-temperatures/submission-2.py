class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # (temp, index)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_temp, stack_idx = stack.pop()
                res[stack_idx] = (i - stack_idx)

            stack.append([t, i])

        return res























        # result = []

        # for i in range(len(temperatures)):
        #     count = 0
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             count += 1
        #             result.append(count)
        #             break
        #         elif j == len(temperatures) - 1:
        #             # at this point no further element so no greater element therefore 0 is appended
        #             result.append(0)
        #         count += 1


        # # for last one
        # result.append(0)
        # return result