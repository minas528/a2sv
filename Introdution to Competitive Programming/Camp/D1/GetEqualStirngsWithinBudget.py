class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        i = -1
        j = 0
        cur = abs(ord(s[0]) - ord(t[0]))
        mx = -1
        while j < len(s):
            if cur <= maxCost:
                mx = max(mx, j - i)
                j += 1
                if j == len(s):
                    break
                cur += abs(ord(s[j]) - ord(t[j]))
            else:
                i += 1
                cur -= abs(ord(s[i]) - ord(t[i]))

        return mx if mx != -1 else 0