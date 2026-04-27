class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        return ''.join(str(len(word)) + "#" + word for word in strs)

    def decode(self, s: str) -> List[str]:
        i, length = 0, len(s)
        ans = []
        builder = ''
        while i < length:
            if s[i] == '#':
                builder = int(builder)
                word = []
                while builder > 0:
                    i += 1
                    word.append(s[i])
                    builder -= 1
                ans.append(''.join(word))

                builder = ''
            else:
                builder += s[i]
            i += 1
        return ans
