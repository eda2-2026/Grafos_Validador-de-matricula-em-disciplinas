import streamlit as st

from src.estruturasCurriculares import CURSOS, DISCIPLINAS, get_subjects_by_course
from src.selector import course_selector, subject_checklist
from src.graph_utils import build_reverse_graph, validate_planned_subjects
from html import escape


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

st.header("Curso")
st.write(
    "Selecione o seu curso."
)

selected_course_id = course_selector(CURSOS)
subjects = get_subjects_by_course(selected_course_id)

st.divider()

st.header("Disciplinas do curso selecionado")

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


def get_subject_display_name(subject_code: str, code_to_id: dict) -> str:
    """
    Recebe o código oficial da disciplina e retorna o nome formatado dela.
    """
    subject_id = code_to_id.get(subject_code, subject_code)
    subject = DISCIPLINAS.get(subject_id)

    if subject:
        return subject["name"]

    return subject_id


def get_subject_card_html(subject_code: str, status: str, code_to_id: dict) -> str:
    """
    Cria um card HTML para representar uma disciplina no caminho de dependência.
    """
    subject_name = get_subject_display_name(subject_code, code_to_id)

    status_labels = {
        "completed": "Concluída",
        "missing": "Pré-requisito faltante",
        "target_allowed": "Pretendida liberada",
        "target_blocked": "Pretendida bloqueada",
    }

    status_class = {
        "completed": "card-completed",
        "missing": "card-missing",
        "target_allowed": "card-target-allowed",
        "target_blocked": "card-target-blocked",
    }

    return f"""
        <div class="dependency-card {status_class[status]}">
            <div class="dependency-title">{escape(subject_name)}</div>
            <div class="dependency-code">{escape(subject_code)}</div>
            <div class="dependency-badge">{status_labels[status]}</div>
        </div>
    """


def render_dependency_path(result: dict, completed_subjects: set, code_to_id: dict):
    """
    Renderiza visualmente o caminho de pré-requisitos de uma disciplina planejada.
    """
    cards = []

    for prerequisite_code in reversed(result["prerequisites"]):
        if prerequisite_code in completed_subjects:
            status = "completed"
        else:
            status = "missing"

        cards.append(
            get_subject_card_html(
                subject_code=prerequisite_code,
                status=status,
                code_to_id=code_to_id,
            )
        )

    target_status = "target_allowed" if result["allowed"] else "target_blocked"

    cards.append(
        get_subject_card_html(
            subject_code=result["subject"],
            status=target_status,
            code_to_id=code_to_id,
        )
    )

    path_html = '<div class="dependency-path">'
    path_html += '<div class="dependency-arrow">→</div>'.join(cards)
    path_html += "</div>"

    st.markdown(path_html, unsafe_allow_html=True)


st.markdown(
    """
    <style>
        .dependency-path {
            display: flex;
            align-items: stretch;
            gap: 10px;
            flex-wrap: wrap;
            margin-top: 12px;
            margin-bottom: 24px;
        }

        .dependency-card {
            min-width: 190px;
            max-width: 250px;
            padding: 12px 14px;
            border-radius: 14px;
            border: 1px solid #d1d5db;
            background-color: #ffffff;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
        }

        .dependency-title {
            font-size: 0.92rem;
            font-weight: 700;
            line-height: 1.25;
            margin-bottom: 6px;
            color: #111827;
        }

        .dependency-code {
            font-size: 0.78rem;
            color: #6b7280;
            margin-bottom: 8px;
        }

        .dependency-badge {
            display: inline-block;
            font-size: 0.75rem;
            font-weight: 700;
            padding: 4px 8px;
            border-radius: 999px;
        }

        .dependency-arrow {
            display: flex;
            align-items: center;
            justify-content: center;
            color: #6b7280;
            font-size: 1.5rem;
            font-weight: 700;
            padding: 0 2px;
        }

        .card-completed {
            border-left: 6px solid #16a34a;
            background-color: #f0fdf4;
        }

        .card-completed .dependency-badge {
            color: #166534;
            background-color: #dcfce7;
        }

        .card-missing {
            border-left: 6px solid #f59e0b;
            background-color: #fffbeb;
        }

        .card-missing .dependency-badge {
            color: #92400e;
            background-color: #fef3c7;
        }

        .card-target-allowed {
            border-left: 6px solid #2563eb;
            background-color: #eff6ff;
        }

        .card-target-allowed .dependency-badge {
            color: #1e40af;
            background-color: #dbeafe;
        }

        .card-target-blocked {
            border-left: 6px solid #dc2626;
            background-color: #fef2f2;
        }

        .card-target-blocked .dependency-badge {
            color: #991b1b;
            background-color: #fee2e2;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


code_to_id = {v["code"]: k for k, v in DISCIPLINAS.items()}

if planned_subjects:
    st.divider()
    st.header("Validação de Matrícula")

    subject_codes_in_course = [s["code"] for s in subjects]
    reverse_graph = build_reverse_graph(subject_codes_in_course)
    
    validation_results = validate_planned_subjects(planned_subjects, completed_subjects, reverse_graph)
    
    for result in validation_results:
        subj_code = result["subject"]
        subj_id = code_to_id.get(subj_code, subj_code)
        
        if result["allowed"]:
            st.success(f"A disciplina **{subj_id}** está liberada.")
        else:
            missing_ids = [code_to_id.get(c, c) for c in result["missing"]]
            st.error(f"A disciplina **{subj_id}** está bloqueada. Você precisa cursar antes: **{', '.join(missing_ids)}**.")

    st.divider()
    st.header("Caminhos de Dependência")
    for result in validation_results:
        subject_name = get_subject_display_name(result["subject"], code_to_id)

        st.markdown(f"#### {subject_name}")

        if result["prerequisites"]:
            render_dependency_path(result, completed_subjects, code_to_id)
        else:
            st.info("Esta disciplina não possui pré-requisitos.")
