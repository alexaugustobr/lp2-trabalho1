from core.Aluno import Aluno
from core.Disciplina import Disciplina
from core.Professor import Professor
from core.Matricula import Matricula

def main():
    #1 CRIAR 5 DISCIPLINAS
    matematica = Disciplina()
    portugues = Disciplina()
    historia = Disciplina()
    geografia = Disciplina()
    filosofia = Disciplina()
    
    matematica.altera_nome("matematica")
    portugues.altera_nome("portugues")
    historia.altera_nome("historia")
    geografia.altera_nome("geografia")
    filosofia.altera_nome("filosofia")

    matematica.altera_carga_horaria(1)
    portugues.altera_carga_horaria(1)
    historia.altera_carga_horaria(1)
    geografia.altera_carga_horaria(1)
    filosofia.altera_carga_horaria(1)

    
    
    #2 CRIAR 5 ALUNOS
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

    #3 CRIAR 2 PROFESSORES
    julio = Professor()
    henrique = Professor()

    #4 MATRICULAR 5 ALUNOS A 5 DISCIPLINAS
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

    #5 ADICIONAR 2 DISCIPLINAS PARA UM PROF E 3 PRA OUTRO
    julio.adicionar_disicplina(matematica)
    julio.adicionar_disicplina(portugues)

    

    henrique.adicionar_disicplina(historia)
    henrique.adicionar_disicplina(geografia)
    henrique.adicionar_disicplina(filosofia)

    for d in julio.retorna_disiciplinas():
        print (d)

    for d in henrique.retorna_disiciplinas():
        print (d)

    #6 MOSTRAR DISICPLIONAS DE CADA ALUNO
    for aluno in alunos:
        print (aluno.retorna_nome(),aluno.disciplinas_aluno())

    #7 MOSTRAR CARGA HORARIA DO PROFESSOR

    print(julio.carga_horaria_total())
    print(henrique.carga_horaria_total())

    #8 confimar a matricula de alunos em 5 disciplinas
    for i in range(0,4):
        print(alunos[i].confirmar_matricula(matematica))
        print(alunos[i].confirmar_matricula(portugues))
        print(alunos[i].confirmar_matricula(historia))
        print(alunos[i].confirmar_matricula(geografia))
        print(alunos[i].confirmar_matricula(filosofia))

    #8 confimar a matricula de 1 aluno em 4 disciplina
    print(reginaldo.confirmar_matricula(matematica))
    print(reginaldo.confirmar_matricula(portugues))
    print(reginaldo.confirmar_matricula(historia))
    print(reginaldo.confirmar_matricula(geografia))

    #8 confimar a matricula de 1 aluno em 1 disciplina
    print(reginaldo.confirmar_matricula(filosofia))
    

if __name__ == "__main__":
    main()