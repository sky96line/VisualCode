graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F', 'G']),
         'D': set(['B']),
         'E': set(['B']),
         'F': set(['C']),
         'G': set(['C'])}

result = []
def dfs(graph, start, goal):
  stack = [(start, [start])]
  while stack:
    (vertex, path) = stack.pop(0)
    for next in graph[vertex] - set(path):
      if next is goal:
        yield path + [next]
      else:
        stack.append((next, path + [next]))

path = list(dfs(graph,'A','F'))
print(path)
