"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 

        # 1 [(2)]
        # 2 [(1),(3)]
        # 3 [(2)]

        nodes = {} #[1:(1) , 2:(2), 3:(3)]

        q = deque() # [3]
        q.append(node)
        head = Node(node.val) # [1]
        nodes[node.val] = head

        while q:
            curr = q.popleft() # [3]
            clone = nodes[curr.val]#[3]
            for n in curr.neighbors:
                if n.val not in nodes:
                    q.append(n)
                    nodes[n.val] = Node(n.val)
                clone.neighbors.append(nodes[n.val])
        
        return head


