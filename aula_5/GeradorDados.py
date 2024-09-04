import random
import os

def gerar_nome_aleatorio():
    nomes = ["João", "Maria", "Carlos", "Ana", "Lucas", "Mariana", "Pedro", "Fernanda", "Ricardo", "Julia"]
    sobrenomes = ["Silva", "Souza", "Oliveira", "Pereira", "Costa", "Rodrigues", "Almeida", "Nascimento"]
    return f"{random.choice(nomes)} {random.choice(sobrenomes)}"

def gerar_matricula_aleatoria():
    return random.randint(10000, 99999)

def gerar_curso_aleatorio():
    cursos = ["Sistemas de Informação", "Engenharia de Software", "Ciência da Computação", "Administração", "Direito", "Medicina"]
    return random.choice(cursos)

def gerar_objeto():
    nome = gerar_nome_aleatorio()
    matricula = gerar_matricula_aleatoria()
    curso = gerar_curso_aleatorio()
    return f"{nome}@{matricula}@{curso}"

def gerar_dados(quantidade, nome_arquivo):
    caminho_diretorio = os.path.dirname(os.path.realpath(__file__))
    caminho_completo = os.path.join(caminho_diretorio, f"{nome_arquivo}.txt")
    
    with open(caminho_completo, 'w') as file:
        for _ in range(quantidade):
            objeto = gerar_objeto()
            file.write(objeto + "\n")

    print(f"{quantidade} dados gerados e salvos com sucesso em '{caminho_completo}'.")

def main():
    quantidade = int(input("Quantos dados deseja gerar? "))
    nome_arquivo = input("Digite o nome do arquivo de saída (sem a extensão): ")
    gerar_dados(quantidade, nome_arquivo)

if __name__ == "__main__":
    main()
