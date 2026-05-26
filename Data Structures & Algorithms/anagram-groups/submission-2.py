class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            key = "".join(sorted(s))  # sorted string as key
            if key not in groups:
                groups[key] = []
            groups[key].append(s)

        return list(groups.values())
