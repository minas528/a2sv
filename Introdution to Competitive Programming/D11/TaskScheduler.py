class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        if len(tasks) <= 1 or n == 0:
            return len(tasks)
        frequency_map = dict()
        for task in tasks:
            if task in frequency_map:
                frequency_map[task] += 1
            else:
                frequency_map[task] = 1
        value_list = list(frequency_map.values())
        value_list.sort(reverse=True)
        if len(tasks) / (n + 1) >= value_list[0]:
            return len(tasks)
        else:
            max_cont = 0
            for i in range(len(value_list)):
                if value_list[i] == value_list[0]:
                    max_cont += 1
                else:
                    break
            return (value_list[0] - 1) * (n + 1) + max_cont


if __name__ == '__main__':
    sol = Solution()
    answer = sol.leastInterval(["A", "A", "A", "B", "B", "B"], 2)
    print(answer)
