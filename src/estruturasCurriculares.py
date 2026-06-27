DISCIPLINAS = {
    # Compartilhadas
    "APC": {
        "code": "CIC0004",
        "name": "ALGORITMOS E PROGRAMAÇÃO DE COMPUTADORES",
        "prerequisites": [],
    },
    "EA": {
        "code": "FGA0161",
        "name": "ENGENHARIA E AMBIENTE",
        "prerequisites": [],
    },
    "IE": {
        "code": "FGA0163",
        "name": "INTRODUÇÃO À ENGENHARIA",
        "prerequisites": [],
    },
    "DIAC": {
        "code": "FGA0168",
        "name": "DESENHO INDUSTRIAL ASSISTIDO POR COMPUTADOR",
        "prerequisites": [],
    },
    "C1": {
        "code": "MAT0025",
        "name": "CÁLCULO 1",
        "prerequisites": [],
    },

    "PE": {
        "code": "FGA0157",
        "name": "PROBABILIDADE E ESTATÍSTICA APLICADO A ENGENHARIA",
        "prerequisites": ["C1"],
    },
    "F1": {
        "code": "IFD0171",
        "name": "FISICA 1",
        "prerequisites": [],
    },
    "F1EXP": {
        "code": "IFD0173",
        "name": "FISICA 1 EXPERIMENTAL",
        "prerequisites": [],
    },
    "C2": {
        "code": "MAT0026",
        "name": "CÁLCULO 2",
        "prerequisites": ["C1"],
    },
    "IAL": {
        "code": "MAT0031",
        "name": "INTRODUCAO A ALGEBRA LINEAR",
        "prerequisites": [],
    },

    "ENGECON": {
        "code": "FGA0133",
        "name": "ENGENHARIA ECONÔMICA",
        "prerequisites": [],
    },
    "MÉTODOS": {
        "code": "FGA0160",
        "name": "MÉTODOS NUMÉRICOS PARA ENGENHARIA",
        "prerequisites": ["C2"],
    },
    "HC": {
        "code": "FGA0164",
        "name": "HUMANIDADES E CIDADANIA",
        "prerequisites": [],
    },

    # Compartilhadas sem contar Software
    "MECSOL1": {
        "code": "FGA0154",
        "name": "MECANICA DOS SÓLIDOS 1 PARA ENGENHARIA",
        "prerequisites": ["F1"],
    },
    "QUIMICA TEORICA": {
        "code": "IQD0125",
        "name": "QUIMICA GERAL TEORICA",
        "prerequisites": [],
    },
    "QUIMICA EXPERIMENTAL": {
        "code": "IQD0126",
        "name": "QUIMICA GERAL EXPERIMENTAL",
        "prerequisites": [],
    },
    "C3": {
        "code": "MAT0027",
        "name": "CÁLCULO 3",
        "prerequisites": ["C1"],
    },

    # Aeroespacial
    "CA": {
        "code": "FGA0254",
        "name": "CIÊNCIAS AEROESPACIAIS",
        "prerequisites": [],
    },
    "SA": {
        "code": "FGA0008",
        "name": "SISTEMAS AEROESPACIAIS",
        "prerequisites": ["F1", "CA"],
    },

    # Automotiva
    "ONDULATÓRIA E FÍSICA TÉRMICA": {
        "code": "FGA0090",
        "name": "ONDULATÓRIA E FÍSICA TÉRMICA PARA ENGENHARIA",
        "prerequisites": ["C1", "F1", "F1EXP"],
    },
    "LAB DE ONDULATÓRIA E FÍSICA TÉRMICA": {
        "code": "FGA0107",
        "name": "LABORATÓRIO DE ONDULATÓRIA E FÍSICA TÉRMICA PARA A ENGENHARIA",
        "prerequisites": ["F1", "F1EXP"],
    },
    "DIAC2": {
        "code": "FGA0155",
        "name": "INTRODUÇÃO AO DESIGN E CONCEPÇÃO DE VEÍCULOS",
        "prerequisites": ["DIAC"],
    },

    # Energia

    # Software
    "MD1": {
        "code": "FGA0085",
        "name": "MATEMÁTICA DISCRETA 1",
        "prerequisites": [],
    },
    "OO": {
        "code": "FGA0158",
        "name": "ORIENTAÇÃO A OBJETOS",
        "prerequisites": ["APC"],
    },

    # Eletrônica

    # Software e Eletrônica
    "PED1": {
        "code": "FGA0071",
        "name": "PRÁTICA DE ELETRÔNICA DIGITAL 1",
        "prerequisites": ["IAL"],
    },
    "TED1": {
        "code": "FGA0073",
        "name": "TEORIA DE ELETRÔNICA DIGITAL 1",
        "prerequisites": ["IAL"],
    },
}


CURSOS = {
    "AEROESPACIAL": {
        "name": "Engenharia Aeroespacial",
        "subjects": [
            "APC",
            "EA",
            "IE",
            "DIAC",
            "C1",
            "PE",
            "F1",
            "F1EXP",
            "C2",
            "IAL",
            "ENGECON",
            "MÉTODOS",
            "HC",
            "MECSOL1",
            "QUIMICA TEORICA",
            "QUIMICA EXPERIMENTAL",
            "C3",
            "CA",
            "SA"
        ],
    },
    "AUTOMOTIVA": {
        "name": "Engenharia Automotiva",
        "subjects": [
            "APC",
            "EA",
            "IE",
            "DIAC",
            "C1",
            "PE",
            "F1",
            "F1EXP",
            "C2",
            "IAL",
            "ENGECON",
            "MÉTODOS",
            "HC",
            "MECSOL1",
            "QUIMICA TEORICA",
            "QUIMICA EXPERIMENTAL",
            "C3",
            "ONDULATÓRIA E FÍSICA TÉRMICA",
            "LAB DE ONDULATÓRIA E FÍSICA TÉRMICA",
            "DIAC2"
        ],
    },
    "ENERGIA": {
        "name": "Engenharia de Energia",
        "subjects": [
            "APC",
            "EA",
            "IE",
            "DIAC",
            "C1",
            "PE",
            "F1",
            "F1EXP",
            "C2",
            "IAL",
            "ENGECON",
            "MÉTODOS",
            "HC",
            "MECSOL1",
            "QUIMICA TEORICA",
            "QUIMICA EXPERIMENTAL",
            "C3",
        ],
    },
    "SOFTWARE": {
        "name": "Engenharia de Software",
        "subjects": [
            "APC",
            "EA",
            "IE",
            "DIAC",
            "C1",
            "PE",
            "F1",
            "F1EXP",
            "C2",
            "IAL",
            "ENGECON",
            "MÉTODOS",
            "HC",
            "MD1",
            "OO",
            "PED1",
            "TED1",
        ],
    },
    "ELETRONICA": {
        "name": "Engenharia Eletrônica",
        "subjects": [
            "APC",
            "EA",
            "IE",
            "DIAC",
            "C1",
            "PE",
            "F1",
            "F1EXP",
            "C2",
            "IAL",
            "ENGECON",
            "MÉTODOS",
            "HC",
            "MECSOL1",
            "QUIMICA TEORICA",
            "QUIMICA EXPERIMENTAL",
            "C3",
            "PED1",
            "TED1",
        ],
    },
}


def get_subjects_by_course(course_id: str) -> list[dict]:
    """
    Retorna as disciplinas de um curso.
    """
    course = CURSOS[course_id]

    return [
        DISCIPLINAS[subject_code]
        for subject_code in course["subjects"]
    ]
