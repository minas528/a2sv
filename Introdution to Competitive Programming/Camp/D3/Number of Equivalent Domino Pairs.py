class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        data = {}
        for each in dominoes:
            if (each[0] > each[1]):
                each[0], each[1] = each[1], each[0]

            tmpStr = str(each[0]) + "&" + str(each[1])

            if (tmpStr in data):
                data[tmpStr] += 1
            else:
                data[tmpStr] = 1
        count = 0
        for k, v in data.items():
            tmp = 0
            if (v > 1):
                tmp = (v * (v - 1) // 2)
            count += tmp
        return count
