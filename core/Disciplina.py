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


#NAO MOVER ESSE IMPORT CIRCULAR PARA CIMA
from Matricula import Matricula