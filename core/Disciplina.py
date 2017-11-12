
class Disciplina():
    
    def __init__(self):
        self.__nome = None
        self.__carga_horaria = None
        self.__teoria = None
        self.__pratica = None
        self.__ementa = None
        self. __compentecias = None
        self.__habilidades = None
        self.__conteudo = None
        self.__bibliografia_basica = None
        self.__bibliografia_complementar = None

    def altera_nome(self, nome):
        if type(nome) is not str:
            return False

        self.__nome = nome
        return True

    def altera_carga_horaria(self, carga_horaria):
        if type(carga_horaria) is not int:
            return False

        self.__carga_horaria = carga_horaria
        return True

    def altera_teoria(self, teoria):
        if type(teoria) is not int:
            return False

        self.__teoria = teoria
        return True

    def altera_pratica(self, pratica):
        if type(pratica) is not int:
            return False

        self.__pratica = pratica
        return True

    def altera_ementa(self, ementa):
        if type(ementa) is not str:
            return False

        self.__ementa = ementa
        return True

    def altera_competencias(self, compentecias):
        if type(compentecias) is not str:
            return False

        self.__compentecias = compentecias
        return True

    def altera_habilidades(self, habilidades):
        if type(habilidades) is not str:
            return False

        self.__habilidades = habilidades
        return True

    def altera_conteudo(self, conteudo):
        if type(conteudo) is not str:
            return False

        self.__conteudo = conteudo
        return True

    def altera_bibliografia_basica(self, bibliografia_basica):
        if type(bibliografia_basica) is not str:
            return False

        self.__bibliografia_basica = bibliografia_basica
        return True

    def altera_bibliografia_complementar(self, bibliografia_complementar):
        if type(bibliografia_complementar) is not str:
            return False

        self.__bibliografia_complementar = bibliografia_complementar
        return True

    def retorna_nome( self ):
        return self.__nome

    def retorna_carga_horaria( self ):
        return self.__carga_horaria

    def retorna_teoria( self ):
        return self.__teoria

    def retorna_pratica( self ):
        return self.__pratica

    def retorna_ementa( self ):
        return self.__ementa

    def retorna_competencias( self ):
        return self.__compentecias

    def retorna_habilidades( self ):
        return self.__habilidades

    def retorna_conteudo( self ):
        return self.__conteudo

    def retorna_bibliografia_basica( self ):
        return self.__Bibliografia_Basica

    def retorna_bibliografia_complementar( self ):
        return self.__bibliografia_complementar

    def __str__(self):
        return self.retorna_nome()
from .Matricula import Matricula
from .Pessoa import Pessoa
from .Usuario import Usuario

