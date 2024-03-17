import datetime as dt

from ExerciciosClasses.livro import Livro
from autor import Autor

autor = Autor("Bruno", dt.datetime(1994, 1, 27), "OutroNome")
livro = Livro("1234567890","Livro Teste", "Este é um livro teste.", "1234567891234",dt.datetime.now())


print('-' * 40)
print(autor)
print('-' * 40)
print(livro)
print('-' * 40)