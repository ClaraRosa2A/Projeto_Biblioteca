# Sistema de Gerenciamento de Biblioteca

# Lista que vai guardar todos os livros
livros = []

# Carrega os livros que já foram salvos no arquivo
def carregar_livros():
    try:
        arquivo = open("livros.csv", "r", encoding="utf-8")
        for linha in arquivo:
            linha = linha.strip()
            if linha != "":
                dados = linha.split(";")
                livro = {
                    "titulo": dados[0],
                    "autor": dados[1],
                    "ano": dados[2],
                    "codigo": dados[3],
                    "status": dados[4]
                }
                livros.append(livro)
        arquivo.close()
    except FileNotFoundError:
        # Se o arquivo ainda não existir, começa com a lista vazia
        pass

# Salva todos os livros no arquivo
def salvar_livros():
    arquivo = open("livros.csv", "w", encoding="utf-8")
    for livro in livros:
        linha = (
            livro["titulo"] + ";" +
            livro["autor"] + ";" +
            livro["ano"] + ";" +
            livro["codigo"] + ";" +
            livro["status"] + "\n"
        )
        arquivo.write(linha)
    arquivo.close()
 
# Cadastra um novo livro
def cadastrar_livro():
    print("\n--- CADASTRAR LIVRO ---")
 
    titulo = input("Digite o título: ")
    autor = input("Digite o autor: ")
    ano = input("Digite o ano de publicação: ")
    codigo = input("Digite o código/ISBN: ")
 
    # Todo livro novo começa como disponível
    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "codigo": codigo,
        "status": "Disponível"
    }
    livros.append(livro)
    salvar_livros()
    print("Livro cadastrado com sucesso!")

