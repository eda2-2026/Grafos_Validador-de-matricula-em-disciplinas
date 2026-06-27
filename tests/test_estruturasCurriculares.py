from src.estruturasCurriculares import DISCIPLINAS, CURSOS, get_subjects_by_course


def test_all_subjects_have_required_fields():
    for subject_key, subject in DISCIPLINAS.items():
        assert "code" in subject
        assert "name" in subject
        assert "prerequisites" in subject

        assert isinstance(subject_key, str)
        assert isinstance(subject["code"], str)
        assert isinstance(subject["name"], str)
        assert isinstance(subject["prerequisites"], list)


def test_all_official_subject_codes_are_unique():
    official_codes = [
        subject["code"]
        for subject in DISCIPLINAS.values()
    ]

    assert len(official_codes) == len(set(official_codes))


def test_all_prerequisites_exist_in_catalog():
    for subject in DISCIPLINAS.values():
        for prerequisite in subject["prerequisites"]:
            assert prerequisite in DISCIPLINAS


def test_all_courses_have_required_fields():
    for course in CURSOS.values():
        assert "name" in course
        assert "subjects" in course

        assert isinstance(course["name"], str)
        assert isinstance(course["subjects"], list)


def test_all_course_subjects_exist_in_catalog():
    for course in CURSOS.values():
        for subject_key in course["subjects"]:
            assert subject_key in DISCIPLINAS


def test_courses_do_not_have_duplicated_subjects():
    for course in CURSOS.values():
        subjects = course["subjects"]

        assert len(subjects) == len(set(subjects))


def test_course_subject_prerequisites_are_also_in_the_course():
    for course in CURSOS.values():
        course_subjects = set(course["subjects"])

        for subject_key in course["subjects"]:
            subject = DISCIPLINAS[subject_key]

            for prerequisite in subject["prerequisites"]:
                assert prerequisite in course_subjects


def test_get_subjects_by_course_returns_correct_number_of_subjects():
    for course_id, course in CURSOS.items():
        subjects = get_subjects_by_course(course_id)

        assert len(subjects) == len(course["subjects"])


def test_get_subjects_by_course_returns_valid_subjects():
    subjects = get_subjects_by_course("SOFTWARE")

    for subject in subjects:
        assert "code" in subject
        assert "name" in subject
        assert "prerequisites" in subject
