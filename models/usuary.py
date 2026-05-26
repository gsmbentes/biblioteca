class Usuario:
    def __init__(self, nome, id_usuario):
        if not str(id_usuario).isdigit() or len(str(id_usuario)) != 4:
            raise ValueError("O ID do usuário deve ter exatamente 4 caracteres.")
        self.nome = nome
        self.id_usuario = id_usuario