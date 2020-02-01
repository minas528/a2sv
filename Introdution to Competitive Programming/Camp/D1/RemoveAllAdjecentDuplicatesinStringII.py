class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        ctr =0
        while True:
            i = 0
            val =''
            while i <= len(s)-k:
                screen = s[i]*k
                if s[i:i+k] == screen:
                    i = i+k
                    continue
                else:
                    val += s[i]
                    i+=1
            val+=s[i:i+k]
            if val == s:
                return val
            s= val
            ctr+=1
        return val