import collections

def rank_items(groups):
    all_items = set()
    for group in groups:
        for items in group:
            all_items.add(items)
            
    graph = {items: set() for items in all_items}
    
    for group in groups:
        a, b, c, d = group
        graph[a].add(b)
        graph[a].add(c)
        graph[a].add(d)
        graph[b].add(c)
        graph[b].add(d)
        graph[c].add(d)
    
    worse_sets = {}
    for items in all_items:
        visited = set()
        queue = collections.deque()
        for neighbor in graph[items]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        worse_sets[items] = visited
        
    ranked_items = sorted(all_items, key=lambda x: len(worse_sets[x]), reverse=True)
    return ranked_items

# # Example usage with the tournament groups
# groups = [
#     (1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12), (13, 14, 15, 16),
#     (1, 5, 9, 13), (2, 6, 10, 14), (3, 7, 11, 15), (4, 8, 12, 16),
#     (1, 6, 11, 16), (2, 5, 12, 15), (3, 8, 9, 14), (4, 7, 10, 13),
#     (1, 7, 12, 14), (2, 8, 11, 13), (3, 5, 10, 16), (4, 6, 9, 15)
# ]

# ranking = rank_items(groups)
# print("Final Ranking (best to worst):", ranking)