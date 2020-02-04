class State:
    def __init__(self):
        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0
        self.distance = 0

class Solution:
    def minimumMoves(self, grid):
        neighbors = [[0, 1, 0, 1],
                           [1, 0, 1, 0],
                           [0, 0, 1, -1],
                           [0, 0, -1, 1]];

        N = len(grid)
        start, end = State(),State()
        start.x1 = 0
        start.y1 = 0
        start.x2 = 0
        start.y2 = 1
        end.x1 = N - 1
        end.y1 = N - 2
        end.x2 = N - 1
        end.y2 = N - 1
        start.distance = 0
        q =[]
        visited = set()
        q.insert(0,start)
        visited.add(start)


        while (q != None) :
            current = q.pop()

            for i in range(4):
                neighbor = State()
                neighbor.x1 = current.x1 + neighbors[i][0]
                neighbor.y1 = current.y1 + neighbors[i][1]
                neighbor.x2 = current.x2 + neighbors[i][2]
                neighbor.y2 = current.y2 + neighbors[i][3]
                neighbor.distance = current.distance + 1
                if (self.inSideFree(neighbor, grid, i, N)
                    and neighbor not in visited):
                    # print("Now here",neighbor.x1,end.x1)
                    q.insert(0,neighbor)
                    visited.add(neighbor)
                    if (neighbor.x1 == end.x1 and neighbor.y1 == end.y1
                        and neighbor.x2 == end.x2 and neighbor.y2 == end.y2) :
                        print("here")
                        return neighbor.distance

    def inSideFree(self,neigbhor: State,grid,neighbor_no,N):
        if (neigbhor.x1 < 0 or neigbhor.x1 >= N or
           neigbhor.x2 < 0 or neigbhor.x2 >= N or
           neigbhor.y1 < 0 or neigbhor.y1 >= N or
           neigbhor.y2 < 0 or neigbhor.y2 >= N or
           grid[neigbhor.x1][neigbhor.y1] or
           grid[neigbhor.x2][neigbhor.y2]) :
            return False
        if neighbor_no == 2:
            if (grid[neigbhor.x2][neigbhor.y2+1] or neigbhor.y1 != neigbhor.y2):
                return False
        if (neighbor_no == 3) :
            if (grid[neigbhor.x2+1][neigbhor.y2] or neigbhor.y1 == neigbhor.y2) :
                return False
        return True
if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumMoves([[0,0,0,0,0,1],
               [1,1,0,0,1,0],
               [0,0,0,0,1,1],
               [0,0,1,0,1,0],
               [0,1,1,0,0,0],
               [0,1,1,0,0,0]]))