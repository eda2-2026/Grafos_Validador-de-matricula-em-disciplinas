from src.estruturasCurriculares import DISCIPLINAS
from src.graph_utils import build_reverse_graph

subjects = [v["code"] for k, v in DISCIPLINAS.items()]
rev_graph = build_reverse_graph(subjects)
code_to_id = {v["code"]: k for k, v in DISCIPLINAS.items()}

def dfs_paths(graph, start):
    paths = []
    def dfs(node, path):
        neighbors = graph.get(node, [])
        if not neighbors:
            paths.append(path)
            return
        for neighbor in neighbors:
            dfs(neighbor, path + [neighbor])
    
    dfs(start, [start])
    return paths

print("Paths for FGA0244:")
paths = dfs_paths(rev_graph, "FGA0244")
for p in paths:
    print([code_to_id.get(x, x) for x in p])
