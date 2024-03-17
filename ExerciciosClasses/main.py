import datetime as dt

from editora import Editora
from livro import Livro
from autor import Autor

autor = Autor("Bruno", dt.datetime(1994, 1, 27), "OutroNome")
livro1 = Livro("1234567890", "Livro Teste", "Este é um livro teste.", "1234567891234", dt.datetime.now())
livro2 = Livro("1234567890", "Livro Teste", "Este é um livro teste.", "1234567891234", dt.datetime.now())
autor.adicionar_trabalho(livro1)
livro1.add_autor(autor)
autor.adicionar_trabalho(livro2)
livro2.add_autor(autor)

editora = Editora("1234567890", "Editora Exemplo", "Exemplo Fantasia", "exemplo@email.com")
editora.publicar(livro1)
editora.publicar(livro2)


print('-' * 40)
print(autor)
print('-' * 40)
print(editora)
