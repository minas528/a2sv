class LCS:
    def LCSstring(self,string_1,string_2,n,m):
        if n == 0 or m ==0:
            return 0
        if string_1[n-1]== string_2[m-1]:
            return self.LCSstring(string_1,string_2,n-1,m-1) + 1
        else:
            return max(self.LCSstring(string_1,string_2,n-1,m),self.LCSstring(string_1,string_2,n,m-1))


if __name__ == '__main__':
    lcs = LCS()
    A = "ABCBDAB"
    B = "BDCABAC"
    print(lcs.LCSstring(A,B,len(A),len(B)))
