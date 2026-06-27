import streamlit as st


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
