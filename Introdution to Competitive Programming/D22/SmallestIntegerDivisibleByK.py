class Solution:
    def smallestRepunitDivByK(self,k):
        digit = k%10
        if digit != 1 and digit != 3 and digit != 7 and digit !=9:
            return -1
        list = []
        count = 1
        remainder = 1%k

        while(remainder):
            remainder = (10 * remainder + 1) %k
            count +=1
        return count

# if __name__ == '__main__':
#     print(smallestReputDivbyK(1))
#     print(smallestReputDivbyK(2))
#     print(smallestReputDivbyK(3))
