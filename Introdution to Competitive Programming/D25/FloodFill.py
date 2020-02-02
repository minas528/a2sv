class Solution:
    def floodFill(self, image, sr, sc, newColor):
        if image == [] or image == [[]]:
            return image

        col = len(image) - 1
        row = len(image[0]) - 1
        nbrs = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        visited = set()
        color = image[sr][sc]

        def isValid(i, j):
            if 0 <= i <= col and 0 <= j <= row  and\
                    (i, j) not in visited and\
                    image[i][j] == color:
                return True
            return False

        def dfs(sr, sc):
            image[sr][sc] = newColor
            visited.add((sr, sc))
            for i in nbrs:
                cr = sr + i[0]
                cc = sc + i[1]
                if isValid(cr, cc)  :
                    print("got here", cr, cc)
                    dfs(cr, cc)

        dfs(sr, sc)
        return image
if __name__ == '__main__':
    sol = Solution()
    print(sol.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))