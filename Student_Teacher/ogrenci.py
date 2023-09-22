class Ogrenci:
    def __init__(self, name, surname, studentId):
        self.studentId = studentId
        self.name = name
        self.surname = surname

    def ogrenciListele(self):
        return [self.name, self.surname, self.studentId]

    def ogrenciGuncelle(self, name, surname, studentId):
        self.name = name
        self.surname = surname
        self.studentId = studentId
