from livro import Livro
import datetime


class Editora:
    """Classe para descrição de uma Editora bádica"""

    __slots__ = ['__cod', '__razao_social', '__nome_fantasia', '__email', '__livros']

    def __init__(self, cod: str, razao_social: str, nome_fantasia: str = None, email: str = None):
        self.__cod = cod
        self.__razao_social = razao_social
        self.__nome_fantasia = nome_fantasia
        self.__email = email
        self.__livros = []

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
    def razao_social(self) -> str:
        return self.__razao_social

    @razao_social.setter
    def razao_social(self, razao_social: str) -> None:
        if isinstance(razao_social, str) and 10 <= len(razao_social) <= 150:
            self.__razao_social = razao_social
        else:
            raise ValueError("Razão social deve possuir de 10 a 150 caracteres")

    @property
    def nome_fantasia(self) -> str:
        return self.__nome_fantasia

    @nome_fantasia.setter
    def nome_fantasia(self, nome_fantasia: str) -> None:
        if isinstance(nome_fantasia, str) and 10 <= len(nome_fantasia) <= 150:
            self.__nome_fantasia = nome_fantasia
        else:
            raise ValueError("Nome Fantasia deve possuir de 10 a 150 caracteres")

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str) -> None:
        if not hasattr(email, "__email"):
            self.__email = None
        if isinstance(email, str) and "@" in email or email is None:
            self.__email = email
        else:
            raise ValueError("Email no formato inválido")

    def listar_livros(self) -> list:
        return self.__livros

    def publicacao(self, livro: Livro) -> None:
        try:
            if isinstance(livro, Livro):
                livro.editora = self
                livro.publicacao = datetime.date.today()
                self.__livros.append(livro)
        except Exception as e:
            raise e

    def __str__(self) -> str:
        return f"Editora: {self.__razao_social}"
