class Pessoa():
    nome = None
    email = None
    celular = None

    def __init__(self):
        pass

    def altera_celular(self, celular):
        if type(celular) is not str:
            return False
        self.__celular = celular
        return True
    
    