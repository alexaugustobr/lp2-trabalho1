class Pessoa():
    nome = None
    email = None
    celular = None


    def altera_celular(self, celular):
        if type(celular) is not str:
            return False
        self.celular = celular
        return True
    
    def altera_email(self, email):
        if type(email) is not str:
            return False
        self.email = email
        return True

    def altera_nome(self, nome):
        if type(nome) is not str:
            return False
        self.nome = nome
        return True

    def retorna_celular(self):
        return self.celular

    def retorna_email(self):
        return self.email

    def retorna_nome(self):
        return self.nome
