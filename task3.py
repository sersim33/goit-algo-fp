import networkx as nx
import heapq
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()


# Додавання ребер з вагами
edges_with_weights = [('A', 'B', {'weight': 5}), 
                      ('B', 'C', {'weight': 10}), 
                      ('A', 'C', {'weight': 8}), 
                      ('B', 'D', {'weight': 7}), 
                      ('D', 'E', {'weight': 6}), 
                      ('A', 'D', {'weight': 9}), 
                      ('D', 'F', {'weight': 5}), 
                      ('A', 'F', {'weight': 4})]

G.add_edges_from(edges_with_weights)

# реалізація Dijkstra
def dijkstra(graph, start):
    shortest = {vertex: float('infinity') for vertex in graph}
    shortest[start] = 0
    pq = [(0,start)]

    while pq:
        # print("shortest:", shortest)
        # print(pq)
        current_distance, current_vertex = heapq.heappop(pq)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']
            if distance < shortest[neighbor]:
                shortest[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return shortest

# Visualization of the graph
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(G, pos, with_labels=True, node_size=700, font_size=9, node_color='skyblue', edge_color='gray')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})  # Include edge labels
plt.title("Network Graph")
plt.show()

# Виклик функції Dijkstra
result = dijkstra(G, 'A')

# Відсортуємо результати за відстанями
sorted_result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1])}

# Виведемо відсортовані результати
print(sorted_result)