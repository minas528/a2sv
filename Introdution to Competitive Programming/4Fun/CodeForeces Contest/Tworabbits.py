def main(lst):
    inp_list = []
    for j in lst:
        inp_list.append(j)
    diff = inp_list[1] - inp_list[0]
    total_move = 0
    x = 1
    first_rabbit, second_rabbit = inp_list[3], inp_list[2]
    while total_move < diff:
        total_move = x * first_rabbit + x * second_rabbit

        x += 1
        print(x,total_move)
    if total_move == diff:
        return x-1
    return -1


if __name__ == '__main__':
    size = int(input())
    for i in range(size):
        inp = map(int,input().split(" "))
        print(main(inp))

