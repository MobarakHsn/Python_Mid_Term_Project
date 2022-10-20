import copy
graph={}
graph[1]=[2]
g=copy.deepcopy(graph)
g[1].pop();
print(graph)