class Solution:
    def shortestAlternatingPaths(self, n, red_edges, blue_edges) :
        result = {n,-1}
        b_edges,r_adges ={{}},{{}}

        for i in range(len(red_edges)):
            r_adges[red_edges[i][0]]
