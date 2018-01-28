from dyplomowanie.model.NauczycielAkademicki import NauczycielAkademicki


class TestNauczyciel:

    def test_student_str(self):
        nauczyciel = NauczycielAkademicki(
            login="login",
            haslo="haslo",
            imie="Jan",
            nazwisko="Kowalski",
            sumagodzin=0
        )
        assert nauczyciel.__str__() == "Jan Kowalski"
