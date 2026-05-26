class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []

        for i in range(len(temperatures)):
            count = 0
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    count += 1
                    result.append(count)
                    break
                elif j == len(temperatures) - 1:
                    result.append(0)
                count += 1


        # for last one
        result.append(0)
        return result