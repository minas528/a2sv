class Solution:
    def invalidTransactions(self, transactions):
        list = []
        for i in range(len(transactions)):
            if int(transactions[i].split(",")[2]) >1000:
                list.append(transactions[i])
        under_minute = {}
        for i in range(len(transactions)):
            for j in range(i+1,len(transactions)):
                if abs(int(transactions[i].split(",")[1]) - int(transactions[j].split(",")[1])) <= 60:
                    if (transactions[i].split(",")[0] == transactions[j].split(",")[0]) and (transactions[i].split(",")[2] != transactions[j].split(",")[2]) and i!=j:
                        if transactions[i] not in list:
                            list.append(transactions[i])
                        if transactions[j] not in list:list.append(transactions[j])
        return list
        # print(transactions[0].split[","])

if __name__ == '__main__':
    sol = Solution()
    print(sol.invalidTransactions(["bob,689,1910,barcelona","alex,696,122,bangkok","bob,832,1726,barcelona","bob,820,596,bangkok","chalicefy,217,669,barcelona","bob,175,221,amsterdam"]))