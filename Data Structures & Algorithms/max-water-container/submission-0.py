class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        best = 0
        while i < j:
            curr = (j - i) * min(heights[i], heights[j])
            best = max(curr, best)
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return best