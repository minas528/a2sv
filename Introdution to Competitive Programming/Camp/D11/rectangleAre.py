class Solution:
    def rectangleArea(self, rectangles) -> int:
        x_prev, y_prev = rectangles[0][0], rectangles[0][1]
        area = 0
        for edges in rectangles:
            area += abs((edges[-1] - max(y_prev, edges[1])) * (edges[-2] - max(x_prev, edges[0])))
            # print("before",x_prev, y_prev, edges[-2], edges[-1])
            x_prev = edges[-2]
            y_prev = edges[-1]
            # print("after",x_prev, y_prev, edges[-2], edges[-1])

        return area % (10 ** 9 + 7)     


if __name__ == '__main__':
    # sol = Solution()
    # print(sol.rectangleArea([[0,0,1,1],[2,2,3,3]]))
    a = [[0, 0, 1, 1], [2, 2, 3, 3]]
    print(set([0, 0, 1, 1]).intersection(set([2, 2, 3, 3])))
