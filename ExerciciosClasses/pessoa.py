class Pessoa:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

    def get_data_nascimento(self):
        return self.data_nascimento

    def set_data_nascimento(self, data_nascimento):
        self.data_nascimento = data_nascimento

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome
