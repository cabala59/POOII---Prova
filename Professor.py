from pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self,codigo, nome, sobrenome):
        super().__init__(nome, sobrenome)
        self.codigo = codigo

    def setCodigo(self, codigo):
        self.codigo = codigo

    def getCodigo(self):
        return self.codigo