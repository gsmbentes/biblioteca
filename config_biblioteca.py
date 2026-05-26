from Liv import Livro
from usuary import Usuario
class Biblioteca:
    def __init__(self, nome_biblioteca):
        self.nome_biblioteca = nome_biblioteca
        self.catalogo_livros = []  
        self.usuarios_cadastrados = {}  

    def normalizar_texto(self, texto):
        return texto.strip().lower()

    def cadastrar_livro(self, livro: Livro):
        for l in self.catalogo_livros:
            mesmo_titulo = self.normalizar_texto(l.titulo) == self.normalizar_texto(livro.titulo)
            mesmo_autor = self.normalizar_texto(l.autor) == self.normalizar_texto(livro.autor)
            if mesmo_titulo and mesmo_autor:
                raise ValueError("Engano! Este livro já está cadastrado na biblioteca.")
        
        self.catalogo_livros.append(livro)
        print(f"Livro '{livro.titulo}' cadastrado com sucesso!")

    def cadastrar_usuario(self, usuario: Usuario):
        if usuario.id_usuario in self.usuarios_cadastrados:
            raise ValueError("Erro: ID já presente no DATABASE.")

        self.usuarios_cadastrados[usuario.id_usuario] = usuario        
        print(f"Usuário {usuario.nome} cadastrado com sucesso!")

    def autenticar_id(self, id_usuario):
        if id_usuario not in self.usuarios_cadastrados:
            raise PermissionError("ID errado. Usuário não reconhecido!")
        return True

    def emprestar_livro(self, titulo_livro, id_usuario):
        self.autenticar_id(id_usuario)
        for livro in self.catalogo_livros:
            if self.normalizar_texto(livro.titulo) == self.normalizar_texto(titulo_livro):
                if livro.disponivel:
                    livro.disponivel = False
                    livro.emprestado_para = id_usuario
                    print(f"Livro '{livro.titulo}' disponível! Empréstimo realizado com sucesso.")
                    return
                else:
                    print(f"O livro '{livro.titulo}' já está emprestado no momento.")
                    return
        
        raise ValueError("Livro não encontrado! Certeza dos dados?")

    def devolver_livro(self, titulo_livro, id_usuario):
        self.autenticar_id(id_usuario)
        for livro in self.catalogo_livros:
            if self.normalizar_texto(livro.titulo) == self.normalizar_texto(titulo_livro):
                if not livro.disponivel:
                    if livro.emprestado_para != id_usuario:
                        raise PermissionError("Este livro foi emprestado para outro usuário.")
                    livro.disponivel = True
                    livro.emprestado_para = None
                    print(f"Livro '{livro.titulo}' devolvido com sucesso!")
                    return
                else:
                    print("Este livro já consta como disponível na biblioteca.")
                    return
                    
        print("Livro não pertence a esta biblioteca.")
