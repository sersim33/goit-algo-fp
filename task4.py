import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(id(self))  # Унікальний ідентифікатор для кожного вузла

def draw_heap(heap_root):
    tree = nx.DiGraph()
    pos = {}
    index = 0

    # Додаємо кореневий вузол
    pos[heap_root.id] = (0, 0)
    tree.add_node(heap_root.id, label=str(heap_root.val), color=heap_root.color)

    # Додаємо інші вузли та ребра
    queue = [heap_root]
    while queue:
        node = queue.pop(0)
        if node.left:
            index += 1
            pos[node.left.id] = (pos[node.id][0] - 1 / (2 ** index), pos[node.id][1] - 1)
            tree.add_node(node.left.id, label=str(node.left.val), color=node.left.color)
            tree.add_edge(node.id, node.left.id)
            queue.append(node.left)
        if node.right:
            index += 1
            pos[node.right.id] = (pos[node.id][0] + 1 / (2 ** index), pos[node.id][1] - 1)
            tree.add_node(node.right.id, label=str(node.right.val), color=node.right.color)
            tree.add_edge(node.id, node.right.id)
            queue.append(node.right)

    # Відображаємо купу
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(10, 7))
    nx.draw(tree, pos=pos, labels=labels, arrows=True, node_size=2000, node_color=colors, font_size=12, font_weight='bold')
    plt.show()

# Приклад використання
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

draw_heap(root)