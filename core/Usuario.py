class Usuario:
    ra = None
    senha = None

    def altera_senha(self, senha):
        if type(senha) is not str:
            return False
        self.senha = senha
        return True

    def altera_ra(self, ra):
        if type(ra) is not str:
            return False
        self.ra = ra
        return True

    def retorna_ra(self):
        return self.ra

    def retorna_senha(self):
        return self.senha