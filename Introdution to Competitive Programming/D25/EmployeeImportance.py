
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id) :
        employee_importance_dict = {}
        neighbor_dict = {}

        for employee in employees:
            id1, importance, subbordinate = employee.id, employee.importance, employee.subordinates
            employee_importance_dict[id1] = importance

            if subbordinate == None:
                neighbor_dict[id1] = []
            neighbor_dict[id1] = subbordinate
        impoertance = 0

        def dfs(nbr_list, id):
            nonlocal impoertance
            if neighbor_dict[id] == None:
                return
            for i in nbr_list[id]:
                dfs(nbr_list, i)
            impoertance += employee_importance_dict[id]

        dfs(neighbor_dict, id)
        return impoertance

if __name__ == '__main__':
    emp = Employee(1,5,[2,3])
    emp2 = Employee(2,3,[])
    emp4 = Employee(3,3,[])
    sol = Solution()
    print(sol.getImportance([emp,emp2,emp4],1))