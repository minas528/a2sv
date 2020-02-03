class Solution:
    def orderlyQueue(self, S: str, K: int) -> str:
        # lst=S.split("")
        result=""
        if(K>1):
            lst=[0]*26
            for i in S:
                ind=ord(i)-ord('a')
                lst[ind]+=1
            for i in range(len(lst)):
                if(lst[i]>0):
                    let=chr(ord('a')+i)
                    result=result+(let*lst[i])
            return result
        let=min(S)
        lst=[]
        for i in range(len(S)):
            if(S[i]==let):
                lst.append(i)
        minimum=S
        for j in lst:
            cur=S[j:len(S)]+S[:j]
            if(cur<minimum):
                minimum=cur
        return minimum