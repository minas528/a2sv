class Solution:
    def __init__(self):
        self.dicts = {}
    def tribonacci(self, n: int) -> int:
        if n in self.dicts: return self.dicts[n]
        if n == 0: self.dicts[0] = 0
        elif n==1 or n ==2: self.dicts[1],self.dicts[2]= 1,1
        else: self.dicts[n]= self.tribonacci(n-3)+self.tribonacci(n-2)+self.tribonacci(n-1)
        return self.dicts[n]
