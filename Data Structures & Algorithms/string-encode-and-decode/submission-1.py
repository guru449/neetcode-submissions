class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""

        for s in strs:
            length = len(s)
            res = res + str(length) + "#" + s
        
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            val = ""
            j = i
            while s[j] != "#":
                val += s[j]
                j += 1
            length = int(val)
            word = s[j+1:j+1 + length] 
            i = j + 1 + length
            res.append(word)
        
        return res
            



