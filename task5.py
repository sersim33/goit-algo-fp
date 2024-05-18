import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from matplotlib.colors import LinearSegmentedColormap

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def build_heap(data):
    heapq.heapify(data)
    return data

def list_to_tree(data, index=0):
    """ Перетворює список у бінарне дерево. """
    if index < len(data):
        node = Node(data[index])
        node.left = list_to_tree(data, 2 * index + 1)
        node.right = list_to_tree(data, 2 * index + 2)
        return node
    return None

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def dfs(node, order):
    if node is None:
        return
    order.append(node)
    dfs(node.left, order)
    dfs(node.right, order)

def bfs(root):
    if root is None:
        return []
    queue = deque([root])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order

def apply_colors(order, cmap):
    n = len(order)
    colors = [cmap(i / n) for i in range(n)]
    for node, color in zip(order, colors):
        node.color = color

# Дані для побудови купи
data = [10, 4, 9, 1, 7, 5, 3]

# Побудова бінарної купи
heap_data = build_heap(data)
print("Heapified data:", heap_data)

# Перетворення списку в дерево
root = list_to_tree(heap_data)

# Обхід в глибину (DFS) та призначення кольорів
dfs_order = []
dfs(root, dfs_order)

# Обхід в ширину (BFS) та призначення кольорів
bfs_order = bfs(root)

# Створення кольорової карти від темних до світлих відтінків
cmap = LinearSegmentedColormap.from_list("custom_cmap", ["darkblue", "skyblue"])

# Застосування кольорів до вузлів дерева на основі DFS
apply_colors(dfs_order, cmap)
print("DFS traversal:", [node.val for node in dfs_order])

# Відображення дерева з кольорами для обходу DFS
draw_tree(root)

# Застосування кольорів до вузлів дерева на основі BFS (для порівняння)
apply_colors(bfs_order, cmap)
print("BFS traversal:", [node.val for node in bfs_order])

# Відображення дерева з кольорами для обходу BFS (заново відобразити дерево)
draw_tree(root)