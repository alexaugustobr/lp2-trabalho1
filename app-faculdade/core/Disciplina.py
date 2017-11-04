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

    def __init__(self):
        pass

#NAO MOVER ESSE IMPORT CIRCULAR PARA CIMA
from Matricula import Matricula