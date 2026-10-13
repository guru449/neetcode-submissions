class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hm = collections.defaultdict(list)

        for s in strs:
            l = []
            for c in s:
                l.append(ord(c) - ord('a'))
            
            hm[tuple(sorted(l))].append(s)
       
        return list(hm.values())

