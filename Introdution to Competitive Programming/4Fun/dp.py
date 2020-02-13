res = ''


def main(name, string):
    global res
    n, m = len(name), len(string)
    if name[n - 1] == string[m - 1]:
        res += name[n - 1]
        main(name[:n - 2], string[m - 2])
    return res


if __name__ == '__main__':
    print(main("ABCCBDA", "BDCABA"))
