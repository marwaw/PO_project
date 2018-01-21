class StudentDTO(object):

    def __init__(self, id, imie, nazwisko, nr_indeksu, temat, deklaracja=False):
        self.id = id
        self.imie = imie
        self.nazwisko = nazwisko
        self.nr_indeksu = nr_indeksu
        self.temat = temat
        self.deklaracja = deklaracja