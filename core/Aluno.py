from Pessoa import Pessoa
from Usuario import Usuario
class Aluno(Pessoa,Usuario):
    sigla_curso = None
    matriculas = []


#NAO MOVER ESSE IMPORT CIRCULAR PARA CIMA
from Disciplina import Disciplina
from Matricula import Matricula