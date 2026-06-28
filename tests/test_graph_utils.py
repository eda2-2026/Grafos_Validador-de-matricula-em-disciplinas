from src.graph_utils import build_graph, build_reverse_graph, dfs, get_all_prerequisites


def test_build_graph_with_real_subjects():
    subject_codes_in_course = [
        "MAT0025",  # Cálculo 1
        "MAT0026",  # Cálculo 2
        "FGA0160",  # Métodos Numéricos para Engenharia
    ]

    graph = build_graph(subject_codes_in_course)

    assert graph["MAT0025"] == ["MAT0026"]
    assert graph["MAT0026"] == ["FGA0160"]
    assert graph["FGA0160"] == []


def test_build_reverse_graph_with_real_subjects():
    subject_codes_in_course = [
        "MAT0025",  # Cálculo 1
        "MAT0026",  # Cálculo 2
        "FGA0160",  # Métodos Numéricos para Engenharia
    ]

    reverse_graph = build_reverse_graph(subject_codes_in_course)

    assert reverse_graph["MAT0025"] == []
    assert reverse_graph["MAT0026"] == ["MAT0025"]
    assert reverse_graph["FGA0160"] == ["MAT0026"]


def test_dfs_visits_start_and_reachable_vertices():
    reverse_graph = {
        "APC": [],
        "OO": ["APC"],
        "EDA1": ["APC"],
        "EDA2": ["EDA1"],
    }

    result = dfs(reverse_graph, "EDA2")

    assert result == ["EDA2", "EDA1", "APC"]


def test_dfs_returns_only_start_when_vertex_has_no_neighbors():
    reverse_graph = {
        "APC": [],
        "OO": ["APC"],
    }

    result = dfs(reverse_graph, "APC")

    assert result == ["APC"]


def test_get_all_prerequisites_returns_direct_and_indirect_prerequisites():
    reverse_graph = {
        "APC": [],
        "EDA1": ["APC"],
        "EDA2": ["EDA1"],
    }

    result = get_all_prerequisites("EDA2", reverse_graph)

    assert result == {"EDA1", "APC"}


def test_get_all_prerequisites_returns_empty_set_when_subject_has_no_prerequisites():
    reverse_graph = {
        "APC": [],
        "EDA1": ["APC"],
    }

    result = get_all_prerequisites("APC", reverse_graph)

    assert result == set()


def test_get_all_prerequisites_with_more_than_one_prerequisite_branch():
    reverse_graph = {
        "C1": [],
        "F1": [],
        "F1EXP": [],
        "ONDULATÓRIA E FÍSICA TÉRMICA": ["C1", "F1", "F1EXP"],
    }

    result = get_all_prerequisites(
        "ONDULATÓRIA E FÍSICA TÉRMICA",
        reverse_graph
    )

    assert result == {"C1", "F1", "F1EXP"}


def test_get_all_prerequisites_using_real_reverse_graph():
    subject_codes_in_course = [
        "MAT0025",  # Cálculo 1
        "MAT0026",  # Cálculo 2
        "FGA0160",  # Métodos Numéricos para Engenharia
    ]

    reverse_graph = build_reverse_graph(subject_codes_in_course)

    result = get_all_prerequisites("FGA0160", reverse_graph)

    assert result == {"MAT0026", "MAT0025"}
