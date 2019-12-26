"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
       
    link to https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/submissions/
  
"""
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        
        for i in range(1,z+1):
            if customfunction.f(i,1)>z:
                return ans
            start, end = 1,z
            while (start <= end):
                
                mid = (start + end ) //2
                if customfunction.f(i,mid) > z:
                    end = mid - 1 
                elif customfunction.f(i,mid) < z:
                    start = mid +1
                if customfunction.f(i,mid) == z:
                    ans.append([i,mid])
                    break
        return ans