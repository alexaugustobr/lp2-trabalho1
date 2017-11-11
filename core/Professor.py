from .Pessoa import Pessoa
from .Usuario import Usuario
from .Disciplina import Disciplina

class Professor(Pessoa,Usuario):
    __apelido = None
    __disciplinas = []

    def adicionar_disicplina(self, disciplina):
        if type(disciplina) is not Disciplina:
            return False
        self.__disciplinas.append(disciplina)
        return True

    def remove_disciplina(self, disciplina):
        if not disciplina in disciplinas:
            return False
        self.__disciplinas.remove(disciplina)
        return True
    
    def disciplinas_professor(self):
        return self.__disciplinas

    def carga_horaria_total(self):
        cht = 0
        for disciplina in self.disciplinas:
            if type(disciplina.carga_horaria) is int:
                cht += self.__disciplina.carga_horaria
        return cht