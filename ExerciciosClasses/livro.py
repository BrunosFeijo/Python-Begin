from datetime import datetime


class Livro:
    def __init__(self, cod: str, titulo: str, resumo: str, isbn: str, publicacao: datetime):
        if not isinstance(cod, str) and len(cod) == 10:
            raise TypeError('Um código deve ser uma string de 10 caracteres')
        if not isinstance(titulo, str) and 1 <= len(titulo) <= 100:
            raise TypeError('Um código deve ser uma string de 1 a 100 caracteres')
        if not isinstance(resumo, str) and 10 <= len(resumo) <= 500:
            raise TypeError('Uma resumo deve ser uma string de 10 a 500 caracteres')
        if not isinstance(isbn, str) and len(isbn) == 13:
            raise TypeError('Um isbn deve ser uma string de 13 caracteres')
        if not isinstance(publicacao, datetime):
            raise TypeError('Um publicacao deve ser um datetime')

        self.cod = cod
        self.titulo = titulo
        self.resumo = resumo
        self.isbn = isbn
        self.publicacao = publicacao

    def __str__(self):
        retorno = f'Código: {self.cod} \nTítulo: {self.titulo} \nResumo: {self.resumo} \nIsbn: {self.isbn} \nPublicacao: {self.publicacao}'

        return retorno