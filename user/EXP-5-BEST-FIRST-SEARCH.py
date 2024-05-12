from queue import PriorityQueue

v = 14

graph = [[] for i in range(v)]

def best_first_search(source,destination,graph):
  pq = PriorityQueue()
  visited = [False] * 14
  visited[source] = True

  pq.put((0,source))

  while pq:
    node = pq.get()[1]
    print(node)
    if node==destination:
      break

    for v,c in graph[node]:
      if visited[v] ==False:
        visited[v] = True
        pq.put((c,v))

def addedge(x,y,cost):
  graph[x].append((y,cost))
  graph[y].append((x,cost))

addedge(0, 1, 3)
addedge(0, 2, 6)
addedge(0, 3, 5)
addedge(1, 4, 9)
addedge(1, 5, 8)
addedge(2, 6, 12)
addedge(2, 7, 14)
addedge(3, 8, 7)
addedge(8, 9, 5)
addedge(8, 10, 6)
addedge(9, 11, 1)
addedge(9, 12, 10)
addedge(9, 13, 2)

source = 0
destination = 9

best_first_search(source,destination,graph)