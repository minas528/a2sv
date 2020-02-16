class Solution:
    def maxDistToClosest(self, seats) -> int:
        start, end, result, temp = 0, 0, 1, 0
        for i, v in enumerate(seats):
            if v == 0:
                end += 1
            elif v == 1:
                end = i
                if seats[start] == 0:
                    result = end - start
                else:
                    temp = (end - start - 1) / 2 if (end - start - 1) % 2 == 0 else (end - start) / 2

                    if temp > result:
                        result = temp
                start = i
            print(start,end,result,temp)

        return int(result) if result > end - start else end - start


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxDistToClosest([1, 0, 0, 0,1]))
