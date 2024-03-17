from datetime import datetime

from ExerciciosClasses import Livro
from ExerciciosClasses import Pessoa


class Autor(Pessoa):
    def __init__(self, nome, data_nascimento, pseudonimo):
        if not isinstance((nome, pseudonimo), str):
            raise TypeError('O nome/pseudonimo deve ser uma string')
        if not isinstance(data_nascimento, datetime):
            raise TypeError('A data de nascimento deve ser do tipo datetime')

        super(nome,data_nascimento)
        self.trabalhos = None
        self.pseudonimo = pseudonimo

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
