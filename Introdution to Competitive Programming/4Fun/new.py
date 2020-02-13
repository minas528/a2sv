def main(nums):
    lst = []
    for i in nums:
        lst.append(i)
    #     print(lst)
    half = 0
    if lst[0] % 2 == 0:
        half = lst[0] // 2
    else:
        half = lst[0] // 2 + (1)
    #     print(half)
    res = half * lst[2] - half * lst[1]
    if lst[0] < lst[1]:
        return lst[0]
    if res == 0:
        return lst[0]
    return res


if __name__ == '__main__':
    a = int(input())
    for i in range(a):
        inp = map(int, input().split())
        print(main(inp))
