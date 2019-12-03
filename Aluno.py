from pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, matricula, nome, sobrenome):
        super().__init__(nome, sobrenome)
        self.matricula = matricula

    def setMatricula(self, matricula):
        self.matricula = matricula

    def getMatricula(self):
        return self.matricula