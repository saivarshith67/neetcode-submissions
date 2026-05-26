class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # counter_s = Counter(s)
        # counter_t = Counter(t)

        # return counter_s == counter_t

        counter_s = [0] * 26
        counter_t = [0] * 26

        for c in s:
            pos = (ord(c) - ord('a'))
            counter_s[pos] += 1

        for c in t:
            pos = (ord(c) - ord('a'))
            counter_t[pos] += 1

        return counter_s == counter_t


        