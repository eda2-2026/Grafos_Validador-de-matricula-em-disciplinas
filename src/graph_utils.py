from typing import Set, List, Dict
from src.estruturasCurriculares import DISCIPLINAS

def build_graph(subject_codes_in_course: List[str]) -> Dict[str, List[str]]:
    """
    Constrói a lista de adjacência (grafo direcionado normal).
    Os vértices são os 'codes' das disciplinas (ex: 'CIC0004').
    Retorna: { 'CIC0004': ['codigo_desbloqueado1', ...], ... }
    """
    code_to_id = {v["code"]: k for k, v in DISCIPLINAS.items()}
    id_to_code = {k: v["code"] for k, v in DISCIPLINAS.items()}
    
    graph = {code: [] for code in subject_codes_in_course}
    
    for code in subject_codes_in_course:
        subj_id = code_to_id.get(code)
        if not subj_id:
            continue
        prereqs = DISCIPLINAS[subj_id].get("prerequisites", [])
        for p in prereqs:
            p_code = id_to_code.get(p)
            if p_code in graph:
                graph[p_code].append(code)
                
    return graph

def build_reverse_graph(subject_codes_in_course: List[str]) -> Dict[str, List[str]]:
    """
    Constrói a lista de adjacência reversa (pré-requisitos).
    Os vértices são os 'codes' das disciplinas (ex: 'CIC0004').
    Retorna: { 'CIC0004': ['prereq1', 'prereq2', ...], ... }
    """
    code_to_id = {v["code"]: k for k, v in DISCIPLINAS.items()}
    id_to_code = {k: v["code"] for k, v in DISCIPLINAS.items()}
    
    reverse_graph = {code: [] for code in subject_codes_in_course}
    
    for code in subject_codes_in_course:
        subj_id = code_to_id.get(code)
        if not subj_id:
            continue
        prereqs = DISCIPLINAS[subj_id].get("prerequisites", [])
        for p in prereqs:
            p_code = id_to_code.get(p)
            if p_code in reverse_graph:
                reverse_graph[code].append(p_code)
                
    return reverse_graph

def dfs(graph: dict[str, list[str]], start: str) -> list[str]:
    """
    Executa uma busca em profundidade (DFS) a partir de um vértice inicial.

    Parâmetros:
        graph: lista de adjacência do grafo.
        start: vértice inicial da busca.

    Retorno:
        Lista com os vértices visitados, na ordem em que foram encontrados.
    """
    visited = set()
    visit_order = []

    def visit(node: str):
        if node in visited:
            return

        visited.add(node)
        visit_order.append(node)

        for neighbor in graph.get(node, []):
            visit(neighbor)

    visit(start)

    return visit_order

def get_all_prerequisites(subject_code: str, reverse_graph: Dict[str, List[str]]) -> Set[str]:
    visited = set()
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in reverse_graph.get(node, []):
            dfs(neighbor)
    dfs(subject_code)
    visited.remove(subject_code) if subject_code in visited else None
    return visited

def get_subgraph_edges(start: str, reverse_graph: Dict[str, List[str]]) -> List[tuple]:
    """
    Retorna uma lista de arestas (tuplas de códigos) percorrendo do nó alvo
    até suas folhas no grafo reverso. Uma aresta (A, B) indica que A é pré-requisito de B.
    """
    edges = set()
    visited = set()
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for prereq in reverse_graph.get(node, []):
            edges.add((prereq, node))
            dfs(prereq)
            
    dfs(start)
    return list(edges)

def validate_planned_subjects(planned: Set[str], completed: Set[str], reverse_graph: Dict[str, List[str]]) -> List[dict]:
    """
    Valida disciplinas planejadas utilizando DFS no grafo reverso.

    Para cada disciplina planejada, busca todos os pré-requisitos diretos
    e indiretos usando DFS e compara com as disciplinas concluídas.
    """
    results = []

    for p_code in planned:
        required = get_all_prerequisites(p_code, reverse_graph)

        missing = required - completed
        
        # Obter as ramificações visuais (arestas/edges)
        edges = get_subgraph_edges(p_code, reverse_graph)
        
        results.append({
            "subject": p_code,
            "allowed": len(missing) == 0,
            "prerequisites": list(required),
            "missing": list(missing),
            "edges": edges
        })
    return results
