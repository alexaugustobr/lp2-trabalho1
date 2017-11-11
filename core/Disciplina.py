
from Pessoa import Pessoa
from Usuario import Usuario


class Disciplina():
    nome = None
    carga_horaria = None
    teoria = None
    pratica = None
    ementa = None
    compentecias = None
    habilidades = None
    conteudo = None
    bibliografia_basica = None
    bibliografia_complementar = None

    def altera_nome(self, nome):
        if type(nome) is not str:
            return False

        self.nome = nome
        return True

    def altera_carga_horaria(self, carga_horaria):
        if type(carga_horaria) is not int:
            return False

        self.carga_horaria = carga_horaria
        return True

    def altera_teoria(self, teoria):
        if type(teoria) is not int:
            return False

        self.teoria = teoria
        return True

    def altera_pratica(self, pratica):
        if type(pratica) is not int:
            return False

        self.pratica = pratica
        return True

    def altera_ementa(self, ementa):
        if type(ementa) is not str:
            return False

        self.ementa = ementa
        return True

    def altera_competencias(self, compentecias):
        if type(compentecias) is not str:
            return False

        self.compentecias = compentecias
        return True

    def altera_habilidades(self, habilidades):
        if type(habilidades) is not str:
            return False

        self.habilidades = habilidades
        return True

    def altera_conteudo(self, conteudo):
        if type(conteudo) is not str:
            return False

        self.conteudo conteudo
        return True

    def altera_bibliografia_basica(self, bibliografia_basica):
        if type(bibliografia_basica) is not str:
            return False

        self.bibliografia_basica = bibliografia_basica
        return True

    def altera_bibliografia_complementar(self, bibliografia_complementar):
        if type(bibliografia_complementar) is not str:
            return False

        self.bibliografia_complementar = bibliografia_complementar
        return True

    def retorna_nome( self ):
        Nome = self.nome
        return Nome

    def retorna_carga_horaria( self ):
        if expression:
            pass
        Carga_Horaria = self.carga_horaria
        return int(Carga_Horaria)

    def retorna_teoria( self ):
        Teoria = self.teoria
        return int(Teoria)

    def retorna_pratica( self ):
        Pratica = self.pratica
        return int(Pratica)

    def retorna_ementa( self ):
        Ementa = self.ementa
        return Ementa

    def retorna_competencias( self ):
        Competencias = self.compentecias
        return Competencias

    def retorna_habilidades( self ):
        Habilidades = self.habilidades
        return Habilidades

    def retorna_conteudo( self ):
        Conteudo = self.conteudo
        return Conteudo

    def retorna_bibliografia_basica( self ):
        Bibliografia_Basica = self.Bibliografia_Basica
        return Bibliografia_Basica

    def retorna_bibliografia_complementar( self ):
        Bibliografia_Complementar = self.bibliografia_complementar
        return Bibliografia_Complementar

from Matricula import Matricula

