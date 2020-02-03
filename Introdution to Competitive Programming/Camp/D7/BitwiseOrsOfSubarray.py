#  while index<len(A):
#             prev.append(A[index])
#             length=len(prev)
#             for i in xrange (length-1,-1,-1):
#                 temp=prev.pop(i)
#                 temp=temp|A[index]
#                 if temp not in record:
#                     record[temp]=set([index])
#                     prev.append(temp)
#                 else:
#                     if index not in record[temp]:
#                         record[temp].add(index)
#                         prev.append(temp)
#             index+=1
#
#         return(len(record))
class Solution:
    def subarrayBitwiseORs(self, A) :
        possible_results, checked = {}, []
        for i in range(len(A)):
            checked.append(A[i])
            for j in range(len(checked) - 1, -1, -1):
                val = checked.pop(j)
                val = val | A[i]
                print(val,A[i],checked,possible_results)
                if val not in possible_results:
                    possible_results[val] = [i]
                    checked.append(val)
                else:
                    if i not in possible_results[val]:
                        possible_results[val].append(i)
                        checked.append(val)

        return len(possible_results)


if __name__ == '__main__':
    sol = Solution()
    print(sol.subarrayBitwiseORs([1,1,2]))