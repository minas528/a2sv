def conTest(string):
        l_count,r_count = 0,0
        for sstr in string:
                if sstr == 'L':
                        l_count +=1
                elif sstr == 'R':
                        r_count +=1
        return l_count+r_count+1

if __name__ == '__main__':
        size = eval(input())
        string = input()
        print(conTest(string))
