from .Pessoa import Pessoa
from .Usuario import Usuario
from .Disciplina import Disciplina

class Professor(Pessoa,Usuario):
    

    def __init__(self):
        self.__apelido = None
        self.__disciplinas = []
        Pessoa.__init__(self)
        Usuario.__init__(self)

    def retorna_disiciplinas(self):
        return self.__disciplinas

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
        for disciplina in self.__disciplinas:
            print (disciplina)
            if type(disciplina.retorna_carga_horaria()) is int:
                cht += disciplina.retorna_carga_horaria()
        return cht