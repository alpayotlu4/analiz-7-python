class Ogretmen:
    def __init__(self, name, surname, teacherId):
        self.name = name
        self.surname = surname
        self.teacherId = teacherId

    def ogretmenListele(self):
        return [self.name, self.surname, self.teacherId]

    def ogretmenGuncelle(self, name, surname, teacherId):
        self.name = name
        self.surname = surname
        self.teacherId = teacherId
