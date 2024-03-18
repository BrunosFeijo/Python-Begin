import datetime as dt

from editora import Editora
from livro import Livro
from autor import Autor

try:
    autor = Autor("Bruno", dt.datetime(1994, 1, 27), "OutroNome")

    livro1 = Livro("1234567890", "Livro Teste 1", "Este é um livro teste.", "1234567891234", dt.datetime.now())
    livro2 = Livro("1234567890", "Livro Teste 2", "Este é um livro teste.", "1234567891234", dt.datetime.now())
    autor.adicionar_trabalho(livro1)
    livro1.add_autor(autor)
    autor.adicionar_trabalho(livro2)
    livro2.add_autor(autor)

    editora = Editora("123457890", "Editora Exemplo", "Exemplo Fantasia", "exemplo@email.com")
    editora.publicar(livro1)
    editora.publicar(livro2)

    livro1.remove_autor(autor)

    print('-' * 40)
    print(autor)
    print('-' * 40)
    print(editora)
    print('-' * 40)
    print(livro1.listar_autores())  # vazio
except ValueError as ve:
    print(ve)
except TypeError as te:
    print(te)
