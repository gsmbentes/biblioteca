
from config_biblioteca  import Biblioteca
from Liv import Livro
from usuary  import Usuario

def iniciar():
    nome_bib = input("Digite o nome da sua Biblioteca: ")
    biblioteca = Biblioteca(nome_bib)

    while True:
        print("\n" + "="*30)
        print(f"    MENU {biblioteca.nome_biblioteca.upper()}    ")
        print("="*30)
        print("[1] Cadastrar Novo Livro")
        print("[2] Cadastrar Novo Usuário")
        print("[3] Pegar Livro Emprestado")
        print("[4] Devolver Livro")
        print("[5] Sair do Sistema")
        print("="*30)
        
        opcao = input("Escolha uma opção (1-5): ")
        print("-" * 30)

        try:
            if opcao == "1":
                print("--- CADASTRO DE LIVRO ---")
                titulo = input("Título do livro: ")
                autor = input("Autor do livro: ")
                ano = input("Ano de publicação: ")
                
                
                novo_livro = Livro(titulo, autor, ano)
                biblioteca.cadastrar_livro(novo_livro)

            elif opcao == "2":
                print("--- CADASTRO DE USUÁRIO ---")
                nome = input("Nome do usuário: ")
                id_user = input("Digite um ID de 4 dígitos: ")
                
                
                novo_usuario = Usuario(nome, id_user)
                biblioteca.cadastrar_usuario(novo_usuario)

            elif opcao == "3":
                print("--- EMPRÉSTIMO DE LIVRO ---")
                id_user = input("Digite seu ID de usuário: ")
                titulo = input("Título do livro que deseja: ")
                
                
                biblioteca.emprestar_livro(titulo, id_user)

            elif opcao == "4":
                print("--- DEVOLUÇÃO DE LIVRO ---")
                titulo = input("Título do livro que está devolvendo: ")
                id_user = input("Digite seu ID: ")
                
                
                biblioteca.devolver_livro(titulo, id_user)

            elif opcao == "5":
                print(f"Fechando o sistema da {biblioteca.nome_biblioteca}. Até logo!")
                break  

            else:
                print("Opção inválida! Digite um número de 1 a 5.")

        except (ValueError, PermissionError) as erro:
            print(f"\n❌ ERRO NO SISTEMA: {erro}")
            
        input("\nPressione ENTER para voltar ao menu...")
if __name__ == "__main__":
    iniciar()
