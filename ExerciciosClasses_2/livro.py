from datetime import date, datetime

Editora = str


class Livro:
    """Classe para a descrição de um livro básico"""

    __slots__ = ["__cod", "__isbn", "__titulo", "__resumo", "__publicacao", "__editora",]

    def __init__(self, cod: str, isbn: str):
        self.__cod = cod
        self.__isbn = isbn
        self.__titulo = None
        self.__resumo = None
        self.__publicacao = None
        self.__editora = None

    @property
    def cod(self) -> str:
        return self.__cod

    @cod.setter
    def cod(self, cod: str) -> None:
        if not hasattr(self, "__cod"):
            self.__cod = None
        if isinstance(cod, str) and len(cod) == 10:
            self.__cod = cod
        else:
            raise ValueError("COD deve possuir 10 caracteres")

    @property
    def isbn(self) -> str:
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn: str) -> None:
        if not hasattr(self, "__isbn"):
            self.__isbn = None
        if isinstance(isbn, str) and len(isbn) == 13:
            self.__isbn = isbn
        else:
            raise ValueError("ISBN deve possuir 13 caracteres")

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str) -> None:
        if isinstance(titulo, str) and 1 <= len(titulo) <= 100:
            self.__titulo = titulo
        else:
            raise ValueError("Título deve possuir entre 1 e 100 caracteres")

    @property
    def resumo(self) -> str:
        return self.__resumo

    @resumo.setter
    def resumo(self, resumo: str) -> None:
        if isinstance(resumo, str) and 10 <= len(resumo) <= 500:
            self.__resumo = resumo
        else:
            raise ValueError("O resumo deve possuir entre 1 e 500 caracteres")

    @property
    def publicacao(self) -> date:
        return self.__publicacao

    @publicacao.setter
    def publicacao(self, publicacao: date) -> None:
        if isinstance(publicacao, date):
            self.__publicacao = publicacao
        else:
            raise TypeError("Publicacao deve ser uma data válida")

    @property
    def editora(self) -> Editora:
        return self.__editora

    @editora.setter
    def editora(self, editora: Editora) -> None:
        self.__editora = editora

    def __str__(self):
        if self.__publicacao is not None:
            publicacao = f"Publicado em {self.__publicacao}"
        else:
            publicacao = "Ainda não publicado"
        return f"{self.isbn}: {self.titulo} - {publicacao}"

