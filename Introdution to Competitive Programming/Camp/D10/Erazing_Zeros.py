def main(string):
    sums = 0
    start = 0
    end = 0
    for i in range(len(string)):
        if string[i] == '1':
            start = i
            break
    for j in range(len(string) - 1, -1, -1):
        if string[j] == '1':
            end = j
            break
    #     print(start,end)
    new_ = string[start:end + 1]
    #     print(new_)
    state = 0
    for char in new_:
        if char == '1':
            state = 1
        if char == '0' and state == 1:
            sums += 1
    return sums


if __name__ == '__main__':
    a = int(input())
    for i in range(a):
        print(main(input()))
