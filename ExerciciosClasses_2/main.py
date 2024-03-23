from livro import Livro
from editora import Editora

exorcista = Livro('1234567890', "1234567893210")
exorcista.titulo = "O Exorcista"

apanhador = Livro('0987654321', "0321654987321")
apanhador.titulo = "O apanhador de sonhos"

editora = Editora("9876543210", "Editora Ltda")

colecao = [exorcista, apanhador]

for livro in colecao:
    print(livro)

print('-' * 50)

for livro in colecao:
    editora.publicar(livro)
    print(livro)

print('-' * 50)

# print(editora.listar_livros())

print('-' * 50)

for livro in editora.listar_livros():
    print(livro)
    print(livro.editora)