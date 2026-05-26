class Livro:
    def __init__(self, titulo, autor, ano):
        if not titulo.strip():
            raise ValueError("O título do livro não pode ficar vazio.")
        if not autor.strip():
            raise ValueError("O autor do livro não pode ficar vazio.")
        
        ano = int(ano)
        if ano <= 0:
            raise ValueError("O ano do livro deve ser maior que zero.")
        
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True
        self.emprestado_para = None
