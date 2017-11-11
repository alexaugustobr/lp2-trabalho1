
from Pessoa import Pessoa
from Usuario import Usuario


class Disciplina():
    __nome = None
    __carga_horaria = None
    __teoria = None
    __pratica = None
    __ementa = None
    __compentecias = None
    __habilidades = None
    __conteudo = None
    __bibliografia_basica = None
    __bibliografia_complementar = None

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

        self.__conteudo conteudo
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
        Nome = self.__nome
        return Nome

    def retorna_carga_horaria( self ):
        if expression:
            pass
        Carga_Horaria = self.__carga_horaria
        return int(Carga_Horaria)

    def retorna_teoria( self ):
        Teoria = self.teoria
        return int(Teoria)

    def retorna_pratica( self ):
        Pratica = self.__pratica
        return int(Pratica)

    def retorna_ementa( self ):
        Ementa = self.__ementa
        return Ementa

    def retorna_competencias( self ):
        Competencias = self.__compentecias
        return Competencias

    def retorna_habilidades( self ):
        Habilidades = self.__habilidades
        return Habilidades

    def retorna_conteudo( self ):
        Conteudo = self.__conteudo
        return Conteudo

    def retorna_bibliografia_basica( self ):
        Bibliografia_Basica = self.__Bibliografia_Basica
        return Bibliografia_Basica

    def retorna_bibliografia_complementar( self ):
        Bibliografia_Complementar = self.__bibliografia_complementar
        return Bibliografia_Complementar

from Matricula import Matricula

