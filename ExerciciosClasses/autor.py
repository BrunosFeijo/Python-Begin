from datetime import datetime

from livro import Livro
from pessoa import Pessoa


class Autor(Pessoa):
    def __init__(self, nome, data_nascimento, pseudonimo):
        if not isinstance(nome, str) or not isinstance(pseudonimo, str):
            raise TypeError('O nome/pseudonimo deve ser uma string')
        if not isinstance(data_nascimento, datetime):
            raise TypeError('A data de nascimento deve ser do tipo datetime')

        super().__init__(nome, data_nascimento)
        self.trabalhos = []
        self.pseudonimo = pseudonimo

    def __str__(self):

        retorno = f'Nome: {self.nome} \nData nascimento: {self.data_nascimento} \nPseudonimo: {self.pseudonimo} \nTrabalhos: {self.trabalhos}'
        if len(self.trabalhos) > 0:
            retorno += f' \nTrabalhos Teste'
        return retorno

    def adicionar_trabalho(self, livro):
        if not isinstance(livro, Livro):
            raise TypeError('O livro precisa ser do tipo Livro')
        self.trabalhos.append(livro)

    def get_trabalhos(self):
        return self.trabalhos

    # def get_nome(self):
    #     return self.nome
    #
    # def set_nome(self, nome):
    #     self.nome = nome

    # def get_data_nascimento(self):
    #     return self.data_nascimento
    #
    # def set_data_nascimento(self, data_nascimento):
    #     self.data_nascimento = data_nascimento

    def get_pseudonimo(self):
        return self.pseudonimo

    def set_pseudonimo(self, pseudonimo):
        self.pseudonimo = pseudonimo
