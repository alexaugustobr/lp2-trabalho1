class Usuario:
    ra = None
    senha = None
        
    def altera_senha(self, senha):
        if type(senha) is not str:
            return False
        self.__senha = senha
        return True