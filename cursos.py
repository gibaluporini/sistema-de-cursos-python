import json
import os

caminho_arquivo = "cursos.json"

# Carrega os cursos salvos, se o arquivo existir
if os.path.exists(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        cursos = json.load(arquivo)
else:
    cursos = []

# Função para salvar os cursos no arquivo JSON
def salvar_cursos():
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(cursos, arquivo, ensure_ascii=False, indent=4)

# Começo do programa
nome = input("Qual é o seu nome? ")

while True:
    print(f"\n=== MENU DE CURSOS DO {nome} ===")
    print("[1] Cadastrar Curso")
    print("[2] Listar Cursos")
    print("[3] Sair")
    print("[4] Buscar Curso por Nome")
    print("[5] Apagar Curso")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome_curso = input(f"Nome do curso, {nome}: ")
        preco = input("Preço do curso: ")
        nota = input("Nota do MEC: ")

        cursos.append({
            "nome_curso": nome_curso,
            "preco": preco,
            "nota": nota
        })
        salvar_cursos()
        print("✅ Curso cadastrado com sucesso!")

    elif opcao == "2":
        print(f"\n=== LISTA DE CURSOS DE {nome.upper()} ===")
        if not cursos:
            print("Nenhum curso cadastrado.")
        else:
            for curso in cursos:
                print()
                print(f"Nome: {curso['nome_curso']}")
                print(f"Preço: {curso['preco']}")
                print(f"Nota: {curso['nota']}")
                print("-" * 30)

    elif opcao == "3":
        print("Saindo... até logo!")
        break

    elif opcao == "4":
        busca = input("Digite o nome do curso: ")
        encontrado = False

        for curso in cursos:
            if curso["nome_curso"].lower() == busca.lower():
                print("\n🔍 Curso encontrado:")
                print(f"Nome: {curso['nome_curso']}")
                print(f"Preço: {curso['preco']}")
                print(f"Nota: {curso['nota']}")
                encontrado = True
                break

        if not encontrado:
            print("❌ Curso não encontrado.")

    elif opcao == "5":
        remover = input("Digite o nome do curso para apagar: ")
        removido = False

        for curso in cursos:
            if curso["nome_curso"].lower() == remover.lower():
                cursos.remove(curso)
                salvar_cursos()
                print(f"✅ Curso '{remover}' removido com sucesso!")
                removido = True
                break

        if not removido:
            print("❌ Curso não encontrado. Nada foi removido.")

    else:
        print("Opção inválida. Tente novamente.")
