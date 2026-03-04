

class Graph:
    def __init__(self, graph):
        self.graph = graph

    def heuristic(self, node):
        h = {
            'A': 4,
            'B': 2,
            'C': 5,
            'D': 0,
            'E': 1
        }
        return h[node]

    def astar(self, start, goal):
        open_list = [start]
        closed_list = []

        g = {start: 0}
        parent = {start: None}

        while open_list:
            current = min(open_list, key=lambda x: g[x] + self.heuristic(x))

            if current == goal:
                path = []
                while current is not None:
                    path.append(current)
                    current = parent[current]
                path.reverse()
                print("Path:", path)
                return

            open_list.remove(current)
            closed_list.append(current)

            for neighbour, cost in self.graph[current]:
                if neighbour in closed_list:
                    continue

                new_cost = g[current] + cost

                if neighbour not in open_list:
                    open_list.append(neighbour)
                elif new_cost >= g.get(neighbour, float('inf')):
                    continue

                g[neighbour] = new_cost
                parent[neighbour] = current

        print("Path not found")


graph_data = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 5), ('E', 2)],
    'C': [('D', 12)],
    'D': [],
    'E': [('D', 1)]
}

g = Graph(graph_data)
g.astar('A', 'D')