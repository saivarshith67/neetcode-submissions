class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            encode_s = f"{len(s)}#{s}"
            res.append(encode_s)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        n = len(s)

        while i < n:
            # 1. Read the length (until we hit '#')
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])

            # 2. Move past '#'
            j += 1

            # 3. Extract the string using the known length
            string = s[j:j+length]
            res.append(string)

            # 4. Move pointer to the next encoded segment
            i = j + length

        return res
