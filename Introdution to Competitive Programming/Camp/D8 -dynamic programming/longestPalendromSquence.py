class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.helper(s, 0, len(s) - 1, {})

    def helper(self, string, first, last, visited):
        if (first, last) in visited:
            return visited[(first, last)]
        if first == last:
            return 1
        if first > last:
            return 0
        if string[first] == string[last]:
            visited[(first, last)] = self.helper(string, first + 1, last - 1, visited) + 2
            return visited[(first, last)]
        visited[(first, last)] = max(self.helper(string, first + 1, last, visited),
                                     self.helper(string, first, last - 1, visited))
        return visited[(first, last)]

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindromeSubseq("bbbab"))