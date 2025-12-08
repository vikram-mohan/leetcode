import heapq

def dijkstra(graph, start, end):
    heap = [(0, start)]
    shortest_path = {node: float('inf') for node in graph} # starting point huge offset for things not visited
    shortest_path[start] = 0

    while heap:
        # visit the next closest
        cost, node = heapq.heappop(heap)

        #update shortest_path from here
        for neighbor, weight in graph[node]:
            new = cost + weight
            if new < shortest_path[neighbor]:
                shortest_path[neighbor] = new
                heapq.heappush(heap, (new, neighbor))
    
    return shortest_path[end]


graph = {
    "A" : [("B", 1),("C", 4)],
    "B" : [("A", 1),("C", 2),("D", 5)],
    "C" : [("A", 4),("B", 2),("D", 1)],
    "D" : [("B", 5),("C", 1)]
}

# answer = {"A":0,"B":1,"C":3,"D":4}, starting point = "A"
print("A->B", dijkstra(graph, "A", "B"))
print("A->D", dijkstra(graph, "A", "D"))
print("C->A", dijkstra(graph, "C", "A"))