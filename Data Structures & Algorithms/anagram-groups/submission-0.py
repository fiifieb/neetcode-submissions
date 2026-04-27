class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        subarrs = {}
        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str in subarrs:
                subarrs[sorted_str].append(s)
            else:
                subarrs[sorted_str] = [s]

        ans = []
        for key in subarrs.keys():
            ans.append(subarrs[key])

        return ans