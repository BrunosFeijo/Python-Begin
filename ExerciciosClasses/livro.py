from datetime import datetime

from genero import Genero


class Livro:
    def __init__(self, cod: str, titulo: str, resumo: str, isbn: str, publicacao: datetime, genero=Genero.FANTASIA):
        if not isinstance(cod, str) or not len(cod) == 10:
            print(len(cod), type(cod))
            raise TypeError(f'Um código deve ser uma string de 10 caracteres.')
        if not isinstance(titulo, str) or not 1 <= len(titulo) <= 100:
            raise TypeError('Um código deve ser uma string de 1 a 100 caracteres')
        if not isinstance(resumo, str) or not 10 <= len(resumo) <= 500:
            raise TypeError('Uma resumo deve ser uma string de 10 a 500 caracteres')
        if not isinstance(isbn, str) or not len(isbn) == 13:
            raise TypeError('Um isbn deve ser uma string de 13 caracteres')
        if not isinstance(publicacao, datetime):
            raise TypeError('Um publicacao deve ser um datetime')

        self.cod = cod
        self.titulo = titulo
        self.resumo = resumo
        self.isbn = isbn
        self.publicacao = publicacao
        self.genero = genero

    def __str__(self):
        retorno = f'Código: {self.cod} \nTítulo: {self.titulo} \nResumo: {self.resumo} \nIsbn: {self.isbn} \nPublicacao: {self.publicacao} \nGenero: {self.genero.value}'

        return retorno

    def get_cod(self):
        return self.cod

    def set_cod(self, cod):
        self.cod = cod

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_resumo(self):
        return self.resumo

    def set_resumo(self, resumo):
        self.resumo = resumo

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn

    def get_publicacao(self):
        return self.publicacao

    def set_publicacao(self, publicacao):
        self.publicacao = publicacao

    def get_genero(self):
        return self.genero

    def set_genero(self, genero):
        self.genero = genero
