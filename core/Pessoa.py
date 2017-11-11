class Pessoa():
    __nome = None
    __email = None
    __celular = None


    def altera_celular(self, celular):
        if type(celular) is not str:
            return False
        self.__celular = celular
        return True
    
    def altera_email(self, email):
        if type(email) is not str:
            return False
        self.__email = email
        return True

    def altera_nome(self, nome):
        if type(nome) is not str:
            return False
        self.__nome = nome
        return True

    def retorna_celular(self):
        return self.__celular

    def retorna_email(self):
        return self.__email

    def retorna_nome(self):
        return self.__nome
