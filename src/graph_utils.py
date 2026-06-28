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

def get_all_prerequisites(subject_key: str, reverse_graph: dict[str, list[str]]) -> list[str]:
    """
    Retorna todos os pré-requisitos diretos e indiretos de uma disciplina.

    A função usa DFS no grafo reverso.

    Exemplo:
        Grafo normal:
            APC -> OO

        Grafo reverso:
            OO -> APC
    """
    visited_subjects = dfs(reverse_graph, subject_key)

    return [
        subject
        for subject in visited_subjects
        if subject != subject_key
    ]

def validate_planned_subjects(planned: Set[str], completed: Set[str],reverse_graph: Dict[str, List[str]]) -> List[dict]:
    """
    Valida disciplinas planejadas utilizando DFS no grafo reverso.

    Para cada disciplina planejada, busca todos os pré-requisitos diretos
    e indiretos usando DFS e compara com as disciplinas concluídas.
    """
    results = []

    for p_code in planned:
        required = get_all_prerequisites(p_code, reverse_graph)

        missing = [
            prerequisite
            for prerequisite in required
            if prerequisite not in completed
        ]

        results.append({
            "subject": p_code,
            "allowed": len(missing) == 0,
            "prerequisites": required,
            "missing": missing,
        })

    return results
