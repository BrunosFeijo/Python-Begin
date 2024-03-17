from datetime import datetime

from ExerciciosClasses import Livro


class Autor():
    def __init__(self, nome, data_nascimento, pseudonimo):
        if not isinstance((nome, pseudonimo), str):
            raise TypeError('O nome/pseudonimo deve ser uma string')
        if not isinstance(data_nascimento, datetime):
            raise TypeError('A data de nascimento deve ser do tipo datetime')

        self.trabalhos = None
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.pseudonimo = pseudonimo

    def adicionar_trabalho(self, livro):
        if not isinstance(livro, Livro):
            raise TypeError('O livro precisa ser do tipo Livro')
        self.trabalhos.append(livro)

    def get_trabalhos(self):
        return self.trabalhos
