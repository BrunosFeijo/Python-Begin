from livro import Livro


class Editora():
    def __init__(self, cod: str, razao_social: str, nome_fantasia='', email=''):
        if not isinstance(cod, str) or not len(cod) == 10:
            raise ValueError('O código da Editora deve ser uma string com 10 caracteres')
        if not isinstance(razao_social, str) or not 10 <= len(razao_social) <= 150:
            raise ValueError('A razão social deve ser uma string de 10 a 150 caracteres')
        if not isinstance(nome_fantasia, str) or not 10 <= len(nome_fantasia) <= 150:
            raise ValueError('O nome fantasia deve ser uma string de 10 a 150 caracteres')
        if not isinstance(email, str):
            raise ValueError('O email deve ser uma string')

        self.cod = cod
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.email = email
        self.livros = []

    def __str__(self):
        info_editora = f"Editora: {self.razao_social}\nCódigo: {self.cod}\nNome Fantasia: {self.nome_fantasia}\nEmail: {self.email}\n"
        if self.livros:
            livros_info = "\nLivros Publicados:\n"
            for livro in self.livros:
                livros_info += f"- {livro.titulo}\n"
            return info_editora + livros_info
        else:
            return info_editora + "Nenhum livro publicado."

    def get_cod(self):
        return self.cod

    def set_cod(self, cod: str):
        self.cod = cod

    def get_razao_social(self):
        return self.razao_social

    def set_razao_social(self, razao_social: str):
        self.razao_social = razao_social

    def get_nome_fantasia(self):
        return self.nome_fantasia

    def set_nome_fantasia(self, nome_fantasia: str):
        self.nome_fantasia = nome_fantasia

    def get_email(self):
        return self.email

    def set_email(self, email: str):
        self.email = email

    def publicar(self, livro: Livro):
        if not isinstance(livro, Livro):
            raise TypeError(f"O objeto precisa ser do tipo Livro")
        self.livros.append(livro)

    def listar_livros(self):
        return self.livros
