# Lesson plan

main.py
```python3
from replit import db

def shortest_path(node1, node2):
  path_list = [[node1]]
  path_index = 0
  # To keep track of previously visited nodes
  previous_nodes = {node1}

  if node1 == node2:
    return path_list[0]

  while path_index < len(path_list):
    current_path = path_list[path_index]
    last_node = current_path[-1]
    next_nodes = []
    for n in db[str(last_node)]['Edges']:
      next_nodes.append(int(n))
    # Search goal node
    if node2 in next_nodes:
        current_path.append(node2)
        output = []
        for step in current_path:
          output.append(db[str(step)]['id'])
        return output
    # Add new paths
    for next_node in next_nodes:
      if not next_node in previous_nodes:
        new_path = current_path[:]
        new_path.append(next_node)
        path_list.append(new_path)
        # To avoid backtracking
        previous_nodes.add(next_node)
    # Continue to next path in list
    path_index += 1
  # No path is found
  return []

print(shortest_path(289, 473))
print(shortest_path(401, 104))
print(shortest_path(580, 740))
```

process.py
```python3
import geojson
from replit import db

db.clear()

with open("waterways_reduced.json") as f:
  gj = geojson.load(f)

#edges = {}
with open("edges") as f:
  lines = f.readlines()
  for g in gj.features:
    id = g['properties']['OBJECTID']
    edges = set([])
    for line in lines:
      edge = line.strip().split(" -- ")
      if int(edge[0]) == id:
        edges.add(edge[1])
      if int(edge[1]) == id:
        edges.add(edge[0])
    g['properties']["Edges"] = list(edges)
    db[id] = g['properties']

```


Original Shortest-Path Code von https://onestepcode.com/graph-shortest-path-python/

```python3
def shortest_path(graph, node1, node2):
    path_list = [[node1]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {node1}

    if node1 == node2:
        return path_list[0]
        
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []
```