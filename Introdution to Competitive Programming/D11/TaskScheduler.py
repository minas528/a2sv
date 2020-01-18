class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if len( tasks ) <=1 or n==0:
            return len( tasks )
        d = dict()
        for i in tasks:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1
        
        vals = d.values()
        vals.sort(reverse=True)
        if len( tasks )/ ( n + 1 ) >= vals[0]:
            return len( tasks )
        else:
            x = 0
            for i in xrange( len( vals ) ):
                if vals[i] == vals[0]:
                    x+=1
                else:
                    break
            print  ( vals[0]-1 ),( n + 1) , x
            return ( vals[0]-1 )*( n + 1) + x
        
