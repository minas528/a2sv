class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        possible_results, checked = {}, []
        for i in range(len(A)):
            checked.append(A[i])
            for j in range(len(checked) - 1, -1, -1):
                val = checked.pop(j)
                val = val | A[i]
                # print(val,A[i],checked,possible_results)
                if val not in possible_results:
                    possible_results[val] = set([i])
                    checked.append(val)
                else:
                    if i not in possible_results[val]:
                        possible_results[val].add(i)
                        checked.append(val)

        return len(possible_results)



if __name__ == '__main__':
    sol = Solution()
    print(sol.subarrayBitwiseORs([1,1,2]))