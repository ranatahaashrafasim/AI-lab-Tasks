print("Part 1: DFS using Stack")

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs_stack(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbour in reversed(graph[node]):
                stack.append(neighbour)

dfs_stack(graph, 'A')


print("\n\nPart 2: Inorder, Preorder, Postorder")

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.left = Node('F')
root.right.right = Node('G')

def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")

print("\nPreorder:")
preorder(root)

print("\nInorder:")
inorder(root)

print("\nPostorder:")
postorder(root)