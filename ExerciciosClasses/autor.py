from datetime import datetime

from pais import Pais
from pessoa import Pessoa


class Autor(Pessoa):
    def __init__(self, nome, data_nascimento, pseudonimo, pais=Pais.BRASIL):
        if not isinstance(nome, str) or not isinstance(pseudonimo, str):
            raise ValueError('O nome/pseudonimo deve ser uma string')
        if not isinstance(data_nascimento, datetime):
            raise ValueError('A data de nascimento deve ser do tipo datetime')

        super().__init__(nome, data_nascimento, pais)
        self.trabalhos = []
        self.pseudonimo = pseudonimo

    def __str__(self):

        retorno = f'Nome: {self.nome} \nData nascimento: {self.data_nascimento} \nPseudonimo: {self.pseudonimo} \nPais: {self.pais}'
        if len(self.trabalhos) > 0:
            retorno += '\n' + "-" * 10 + 'Trabalhos' + "-" * 10
            for trabalho in self.trabalhos:
                retorno += f'\n{trabalho}\n'
                if not trabalho == self.trabalhos[-1]:
                    retorno += '-' * 30
        return retorno

    def adicionar_trabalho(self, livro):
        if not "Livro" == type(livro).__name__:
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
