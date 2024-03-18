import heapq

optimal_tour_length = {
    1: 33523,
    2: 699,
    3: 19,
    4: 937,
    5: 2085,
    6: 291
}

def dijkstra(graph, start, file_index):
    total_distance = 0
    distances = {vertex: float('inf') for vertex in range(1, len(graph) + 1)}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        total_distance += current_distance

        for neighbor, weight in enumerate(graph[current_vertex], start=1):
            if weight > 0:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

    optimal_length = optimal_tour_length.get(file_index)
    percentage_difference = abs(total_distance - optimal_length) / optimal_length * 100

    print(f"Peso total: {total_distance}\nValor esperado: {optimal_length}\nMargem de erro: {percentage_difference:.3f}%")