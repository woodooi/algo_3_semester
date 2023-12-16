import heapq

class Vertex:
    def __init__(self, label):
        self.label = label
        self.outbound_edges = []

class Edge:
    def __init__(self, start_vertex, end_vertex, weight):
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.weight = weight

class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = []

        for start_vertex, neighbors in edges.items():
            current_vertex = self.vertices[start_vertex - 1]

            for neighbor, weight in neighbors:
                end_vertex = self.vertices[neighbor - 1]
                edge = Edge(current_vertex, end_vertex, weight)
                self.edges.append(edge)
                current_vertex.outbound_edges.append(edge)

    def dijkstra(self, start_vertex):
        distances = {vertex: float('inf') for vertex in self.vertices.values()}
        distances[start_vertex] = 0

        priority_queue = [(0, start_vertex)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for edge in current_vertex.outbound_edges:
                neighbor = edge.end_vertex
                new_distance = distances[current_vertex] + edge.weight

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor))

        return distances

def find_optimal_server_location(graph, clients):
    min_max_latency = float('inf')

    for potential_server in graph.vertices.values():
        if potential_server not in clients:
            distances = graph.dijkstra(potential_server)
            max_latency = max(distances[client] for client in clients)
        
            if max_latency < min_max_latency:
                min_max_latency = max_latency

    return min_max_latency

file_path = 'gamsrv.in'
def read_graph_from_file(file_path):
    with open(file_path, 'r') as file:
    
        V, E = map(int, file.readline().split())

        graph = {i: [] for i in range(1, V + 1)}
        
        vertices = {i: Vertex(i) for i in range(V)}
        clients = [int(index) for index in file.readline().split()] 
        
        for _ in range(E):
            v1, v2, weight = map(int, file.readline().split())
            graph[v1].append((v2, weight))
            graph[v2].append((v1, weight))

    return graph, vertices, clients

graph_items, vertices, client_indexes = read_graph_from_file(file_path)

game_server = Graph(vertices, graph_items)

clients = [vertices[index - 1] for index in client_indexes]  

min_max_latency = find_optimal_server_location(game_server, clients)

with open("gamsrv.out", "w") as output_file:
    output_file.write(str(min_max_latency))
