class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = []
        if n%2 ==0:
            num = int((n/2)*(-1))
            while(len(arr)<n):
                arr.append(num)
                if num == -1:
                    num+=2
                else:num+=1
        else:
            num = int((n/2)*(-1))
            while(len(arr)<n):
                arr.append(int(num))
                num+=1
        return arr