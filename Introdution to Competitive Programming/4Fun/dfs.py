def dfs(graph,start):
    visited, stack = set(),[start]
    while stack:
        current = stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            print(graph[current]-visited)
            stack.extend(graph[current]-visited)
    return visited

def dfs2(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs2(graph, next, visited)
    return visited
if __name__ == '__main__':
    graph = {'A': set(['B', 'C']),
             'B': set(['A', 'D', 'E']),
             'C': set(['A', 'F']),
             'D': set(['B']),
             'E': set(['B', 'F']),
             'F': set(['C', 'E'])}
    print(dfs2(graph,'A'))