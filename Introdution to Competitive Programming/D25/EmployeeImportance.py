"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_importance = {}
        adj_list = {}
        
        for employee_details in employees:
            id1, importance, subordinates = employee_details.id, employee_details.importance, employee_details.subordinates
            employee_importance[id1] = importance
            
            if adj_list.get(id1) is None:
                adj_list[id1] = []
                
            adj_list[id1] = subordinates
            
        importance = 0
        
        def dfs(adj_list, id):
            nonlocal importance
            if adj_list.get(id) is None:
                return
            
            for neighbor in adj_list[id]:
                dfs(adj_list, neighbor)
                
            importance += employee_importance[id]
            # print(employee_importance[id])
        
        dfs(adj_list, id)
        return importance
