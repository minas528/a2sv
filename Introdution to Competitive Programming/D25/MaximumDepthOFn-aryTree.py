"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:return 0;
        level = 0
        for child in root.children:
            level = max(level,self.maxDepth(child))
        return level+1
