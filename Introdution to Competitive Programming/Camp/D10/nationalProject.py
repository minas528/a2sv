def main(nums):
    lst = []
    for i in nums:
        lst.append(i)
    import math
    half = math.ceil(lst[0] / 2)
    cycles = math.ceil(half / lst[1])
    t = (cycles - 1) * lst[1] + (cycles - 1) * lst[2]
    r = half % lst[1]
    total = t + r if r > 0 else t + lst[1]
    return max(lst[0], total)


if __name__ == '__main__':
    a = int(input())
    for i in range(a):
        inp = map(int, input().split())
        print(main(inp))