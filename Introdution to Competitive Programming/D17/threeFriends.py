def solve(pos1,pos2,pos3):
  dis = 10000000000
  for i in range(-1,2):
    for j in range(-1,2):
      for k in range(-1,2):
        newPos1 = pos1 +i
        newPos2 = pos2 +j
        newPos3 = pos3 +k

        newdis = abs(newPos1-newPos2) + abs(newPos1-newPos3) + abs(newPos2-newPos3)
        if newdis < dis:
          dis = newdis
  return dis


if __name__ == '__main__':
  N = eval(input())
  
  for i in range(N):
    lst = list(map(int, input().split(" ")))
    print(solve(lst[0],lst[1],lst[2]))
