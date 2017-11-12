class Usuario:
    
    def __init__(self):
        self.__ra = None
        self.__senha = None

    def altera_senha(self, senha):
        if type(senha) is not str:
            return False
        self.__senha = senha
        return True

    def altera_ra(self, ra):
        if type(ra) is not str:
            return False
        self.__ra = ra
        return True

    def retorna_ra(self):
        return self.__ra

    def retorna_senha(self):
        return self.__senha