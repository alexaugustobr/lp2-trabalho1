from core.Aluno import Aluno
from core.Disciplina import Disciplina
from core.Professor import Professor
from core.Matricula import Matricula
def main():

    matematica = Disciplina()
    portugues = Disciplina()
    historia = Disciplina()
    geografia = Disciplina()
    filosofia = Disciplina()

    matematica.nome = "matematica"
    portugues.nome = "portugues"
    historia.nome = "historia"
    geografia.nome = "geografia"
    filosofia.nome = "filosofia"

    alex = Aluno()
    cinthia = Aluno()
    michael = Aluno()
    fabio = Aluno()
    reginaldo = Aluno()  

    alex.altera_nome("alex")
    cinthia.altera_nome("cinthia")
    michael.altera_nome("michael")
    fabio.altera_nome("fabio")
    reginaldo.altera_nome("reginaldo")        

    julio = Professor()
    henrique = Professor()

    matricula1 =  Matricula()
    matricula2 =  Matricula()
    matricula3 =  Matricula()
    matricula4 =  Matricula()
    matricula5 =  Matricula()

    matricula1.altera_disciplina(matematica)
    matricula2.altera_disciplina(portugues)
    matricula3.altera_disciplina(historia)
    matricula4.altera_disciplina(geografia)
    matricula5.altera_disciplina(filosofia)

    alunos = [alex,cinthia,michael,fabio,reginaldo]
    matriculas = [matricula1,matricula2,matricula3,matricula4,matricula5]

    for aluno  in alunos:
        for matricula in matriculas:
            aluno.matricular(matricula)

    julio.adicionar_disicplina(matematica)
    julio.adicionar_disicplina(portugues)

    henrique.adicionar_disicplina(historia)
    henrique.adicionar_disicplina(geografia)
    henrique.adicionar_disicplina(filosofia)

    for aluno in alunos:
        print (aluno.retorna_nome(),aluno.disciplinas_aluno())

if __name__ == "__main__":
    main()