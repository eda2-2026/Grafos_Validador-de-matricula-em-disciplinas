import streamlit as st

from src.estruturasCurriculares import CURSOS, get_subjects_by_course
from src.selector import course_selector, subject_checklist


st.set_page_config(
    page_title="Validador de Matrícula UnB Gama",
    page_icon="🎓",
    layout="wide",
)

st.title("Validador de Matrícula em Disciplinas")

st.write(
    """
    Este trabalho modela as matrizes curriculares dos cursos de Engenharia do campus UnB Gama
    (Engenharia **Aeroespacial**, Engenharia **Automotiva**, Engenharia **de Energia**, Engenharia **de Software**
    e Engenharia **Eletrônica**) como um **grafo direcionado**, onde cada disciplina é um vértice, e cada pré-requisito é uma aresta.
    """
)

st.info(
    """
    **Fluxo da aplicação**

    1. O aluno seleciona sua Engenharia.
    2. O aluno seleciona as disciplinas já concluídas.
    3. O aluno seleciona as disciplinas que pretende cursar.
    4. O sistema utiliza DFS no grafo reverso para buscar pré-requisitos.
    5. A interface mostra se a matrícula planejada é válida ou não.
    """
)

st.divider()

st.subheader("Curso")

selected_course_id = course_selector(CURSOS)
subjects = get_subjects_by_course(selected_course_id)

st.divider()

st.subheader("Disciplinas do curso selecionado")

st.write(
    """
    Marque as disciplinas que você já concluiu e as disciplinas que
    você pretende cursar no próximo semestre.
    """
)

left_column, right_column = st.columns(2)

with left_column:
    completed_subjects = subject_checklist(
        title="Disciplinas concluídas",
        subjects=subjects,
        key_prefix=f"completed_{selected_course_id}",
    )

with right_column:
    planned_subjects = subject_checklist(
        title="Disciplinas pretendidas",
        subjects=subjects,
        key_prefix=f"planned_{selected_course_id}",
    )

st.divider()

st.subheader("Seleção atual")

st.write("**Curso:**", CURSOS[selected_course_id]["name"])
st.write("**Concluídas:**", sorted(completed_subjects))
st.write("**Pretendidas:**", sorted(planned_subjects))

from src.graph_utils import build_reverse_graph, validate_planned_subjects
from src.estruturasCurriculares import DISCIPLINAS

code_to_id = {v["code"]: k for k, v in DISCIPLINAS.items()}

if planned_subjects:
    st.divider()
    st.subheader("Validação de Matrícula")

    subject_codes_in_course = [s["code"] for s in subjects]
    reverse_graph = build_reverse_graph(subject_codes_in_course)
    
    validation_results = validate_planned_subjects(planned_subjects, completed_subjects, reverse_graph)
    
    for result in validation_results:
        subj_code = result["subject"]
        subj_id = code_to_id.get(subj_code, subj_code)
        
        if result["allowed"]:
            st.success(f"**{subj_id}** liberada.")
        else:
            missing_ids = [code_to_id.get(c, c) for c in result["missing"]]
            st.error(f"**{subj_id}** bloqueada. Falta: {', '.join(missing_ids)}.")
