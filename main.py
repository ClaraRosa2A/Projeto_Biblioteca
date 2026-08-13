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

# Empresta um livro pelo código
def emprestar_livro():
    print("\n--- EMPRESTAR LIVRO ---")
    codigo = input("Digite o código/ISBN do livro: ")
    for livro in livros:
        if livro["codigo"] == codigo:
 
            if livro["status"] == "Disponível":
                livro["status"] = "Emprestado"
                salvar_livros()
                print("Livro emprestado com sucesso!")
            else:
                print("Esse livro já está emprestado.")
 
            return
    print("Livro não encontrado.")

# Devolve um livro pelo código
def devolver_livro():
    print("\n--- DEVOLVER LIVRO ---")
    codigo = input("Digite o código/ISBN do livro: ")
    for livro in livros:
        if livro["codigo"] == codigo:
 
            if livro["status"] == "Emprestado":
                livro["status"] = "Disponível"
                salvar_livros()
                print("Livro devolvido com sucesso!")
            else:
                print("Esse livro já está disponível.")
 
            return
    print("Livro não encontrado.")

# Mostra todos os livros
def listar_livros():
    print("\n--- TODOS OS LIVROS ---")

    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return
 
    for livro in livros:
        print("-------------------------")
        print("Título:", livro["titulo"])
        print("Autor:", livro["autor"])
        print("Ano:", livro["ano"])
        print("Código:", livro["codigo"])
        print("Status:", livro["status"])

# Procura um livro pelo título ou autor
def buscar_livro():
    print("\n--- BUSCAR LIVRO ---")
    busca = input("Digite o título ou autor: ").lower()
    encontrou = False
 
    for livro in livros:
        if busca in livro["titulo"].lower() or busca in livro["autor"].lower():
            print("-------------------------")
            print("Título:", livro["titulo"])
            print("Autor:", livro["autor"])
            print("Ano:", livro["ano"])
            print("Código:", livro["codigo"])
            print("Status:", livro["status"])
 
            encontrou = True
    if encontrou == False:
        print("Nenhum livro encontrado.")

# Ordena os livros
def ordenar_livros():
    print("\n--- ORDENAR LIVROS ---")
    print("1 - Por título")
    print("2 - Por autor")
    print("3 - Por ano")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        livros.sort(key=lambda livro: livro["titulo"].lower())
        print("Livros ordenados por título.")
 
    elif opcao == "2":
        livros.sort(key=lambda livro: livro["autor"].lower())
        print("Livros ordenados por autor.")
 
    elif opcao == "3":
        livros.sort(key=lambda livro: livro["ano"])
        print("Livros ordenados por ano.")
 
    else:
        print("Opção inválida.")
