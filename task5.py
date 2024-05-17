import heapq
import colorsys
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque  # Importing deque from collections module

class Node:
    def __init__(self, id):
        self.id = id
        self.left = None
        self.right = None

def add_edges(tree, node, pos):
    if node.left:
        tree.add_edge(node.id, node.left.id)
        pos[node.left.id] = (pos[node.id][0] - 1, pos[node.id][1] - 1)
        tree = add_edges(tree, node.left, pos)
    if node.right:
        tree.add_edge(node.id, node.right.id)
        pos[node.right.id] = (pos[node.id][0] + 1, pos[node.id][1] - 1)
        tree = add_edges(tree, node.right, pos)
    return tree



def depth_first_traversal(node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    yield node

    if node.left and node.left not in visited:
        yield from depth_first_traversal(node.left, visited)
    
    if node.right and node.right not in visited:
        yield from depth_first_traversal(node.right, visited)

def breadth_first_traversal(root):
    if root is None:
        return
    
    queue = deque([root])
    visited = set([root])
    while queue:
        node = queue.popleft()
        yield node
        if node.left and node.left not in visited:
            queue.append(node.left)
            visited.add(node.left)
        if node.right and node.right not in visited:
            queue.append(node.right)
            visited.add(node.right)

def draw_tree_with_traversals(tree_root):
    # Фіксований відтінок зеленого
    hue = 0.3
    # Обійти дерево у глибину та присвоїти кожному вузлу унікальний колір
    dfs_traversal = list(depth_first_traversal(tree_root))
    dfs_colors = {node.id: colorsys.hsv_to_rgb(hue, 1.0, (i + 1) / len(dfs_traversal)) for i, node in enumerate(dfs_traversal)}
    # Обійти дерево у ширину та присвоїти кожному вузлу унікальний колір
    bfs_traversal = list(breadth_first_traversal(tree_root))
    bfs_colors = {node.id: colorsys.hsv_to_rgb(hue, 1.0, (i + 1) / len(bfs_traversal)) for i, node in enumerate(bfs_traversal)}

    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [dfs_colors[node[0]] for node in tree.nodes(data=True)]  # Кольори за глибинним обходом
    labels = {node: node for node in tree.nodes()}


    plt.figure(figsize=(16, 8))

    plt.subplot(1, 2, 1)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title("Depth First Traversal")

    colors = [bfs_colors[node[0]] for node in tree.nodes(data=True)]  # Кольори за обходом у ширину

    plt.subplot(1, 2, 2)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title("Breadth First Traversal")

    plt.show()

# Використання:
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

draw_tree_with_traversals(root)