import threading
import os
import time

class Aluno:
    """
    Classe que representa um Aluno com atributos nome, matrícula e curso.
    """
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    def __repr__(self):
        return f"{self.nome}@{self.matricula}@{self.curso}"

class GerenciadorDeAlunos:
    """
    Classe que gerencia a leitura, ordenação e salvamento de dados dos alunos.
    """
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.alunos = self.ler_arquivo()

    def ler_arquivo(self):
        """
        Lê o arquivo e cria uma lista de objetos Aluno.
        """
        alunos = []
        with open(self.arquivo, 'r') as file:
            for linha in file:
                nome, matricula, curso = linha.strip().split('@')
                alunos.append(Aluno(nome, matricula, curso))
        return alunos

    def ordenar(self, chave_primaria, metodo):
        """
        Ordena a lista de alunos de acordo com a chave primária e método de ordenação escolhido.
        Considera a ordenação secundária por matrícula e curso em caso de empates.
        """
        if metodo == "sort":
            self.alunos.sort(key=lambda aluno: (getattr(aluno, chave_primaria), getattr(aluno, 'matricula'), getattr(aluno, 'curso')))
        elif metodo == "bolha":
            self.ordenar_bolha(chave_primaria)
        elif metodo == "selecao":
            self.ordenar_selecao(chave_primaria)
        elif metodo == "insercao":
            self.ordenar_insercao(chave_primaria)

    def ordenar_bolha(self, chave_primaria):
        """
        Ordena a lista de alunos usando o algoritmo de ordenação por Bolha (Bubble Sort).
        Considera a ordenação secundária por matrícula e curso em caso de empates.
        """
        n = len(self.alunos)
        for i in range(n):
            for j in range(0, n-i-1):
                aluno1 = self.alunos[j]
                aluno2 = self.alunos[j+1]
                if getattr(aluno1, chave_primaria) > getattr(aluno2, chave_primaria):
                    self.alunos[j], self.alunos[j+1] = self.alunos[j+1], self.alunos[j]
                elif getattr(aluno1, chave_primaria) == getattr(aluno2, chave_primaria):
                    if aluno1.matricula > aluno2.matricula:
                        self.alunos[j], self.alunos[j+1] = self.alunos[j+1], self.alunos[j]
                    elif aluno1.matricula == aluno2.matricula:
                        if aluno1.curso > aluno2.curso:
                            self.alunos[j], self.alunos[j+1] = self.alunos[j+1], self.alunos[j]

    def ordenar_selecao(self, chave_primaria):
        """
        Ordena a lista de alunos usando o algoritmo de ordenação por Seleção (Selection Sort).
        Considera a ordenação secundária por matrícula e curso em caso de empates.
        """
        n = len(self.alunos)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                aluno1 = self.alunos[j]
                aluno2 = self.alunos[min_idx]
                if getattr(aluno1, chave_primaria) < getattr(aluno2, chave_primaria):
                    min_idx = j
                elif getattr(aluno1, chave_primaria) == getattr(aluno2, chave_primaria):
                    if aluno1.matricula < aluno2.matricula:
                        min_idx = j
                    elif aluno1.matricula == aluno2.matricula:
                        if aluno1.curso < aluno2.curso:
                            min_idx = j
            self.alunos[i], self.alunos[min_idx] = self.alunos[min_idx], self.alunos[i]

    def ordenar_insercao(self, chave_primaria):
        """
        Ordena a lista de alunos usando o algoritmo de ordenação por Inserção.
        Considera a ordenação secundária por matrícula e curso em caso de empates.
        """
        n = len(self.alunos)
        for i in range(1, n):
            j = i-1
            chave_aluno = self.alunos[i]
            while j >= 0 and getattr(self.alunos[j], chave_primaria) > getattr(chave_aluno, chave_primaria):
                self.alunos[j + 1] = self.alunos[j]
                j -= 1
            if j >= 0 and getattr(self.alunos[j], chave_primaria) == getattr(chave_aluno, chave_primaria):
                while j >= 0 and (getattr(self.alunos[j], chave_primaria) == getattr(chave_aluno, chave_primaria) and self.alunos[j].matricula > chave_aluno.matricula):
                    self.alunos[j + 1] = self.alunos[j]
                    j -= 1
                if j >= 0 and (getattr(self.alunos[j], chave_primaria) == getattr(chave_aluno, chave_primaria) and self.alunos[j].matricula == chave_aluno.matricula):
                    while j >= 0 and (getattr(self.alunos[j], chave_primaria) == getattr(chave_aluno, chave_primaria) and self.alunos[j].matricula == chave_aluno.matricula and self.alunos[j].curso > chave_aluno.curso):
                        self.alunos[j + 1] = self.alunos[j]
                        j -= 1
                self.alunos[j + 1] = chave_aluno

    def salvar_em_arquivo(self, nome_arquivo):
        """
        Salva a lista de alunos ordenada em um novo arquivo.
        """
        with open(f"{nome_arquivo}.txt", 'w') as file:
            for aluno in self.alunos:
                file.write(repr(aluno) + "\n")

    def exibir_alunos(self):
        """
        Exibe a lista de alunos no terminal.
        """
        for aluno in self.alunos:
            print(aluno)

def executar_ordenacao(gerenciador, chave_primaria, metodo, nome_arquivo, tempos):
    """
    Função que executa a ordenação em uma thread e mede o tempo de execução.
    """
    start_time = time.time()
    gerenciador.ordenar(chave_primaria, metodo)
    end_time = time.time()
    execution_time = end_time - start_time
    tempos[metodo] = execution_time
    
    # Verifica se é a última thread de ordenação
    if len(tempos) == len(["sort", "bolha", "selecao", "insercao"]):
        gerenciador.salvar_em_arquivo(nome_arquivo)

def main():
    # Nome fixo do arquivo de entrada
    nome_arquivo = "dados.txt"
    
    # Verificar se o arquivo existe
    if not os.path.exists(nome_arquivo):
        print(f"Erro: O arquivo {nome_arquivo} não foi encontrado.")
        return
    
    # Cria o gerenciador de alunos
    gerenciador = GerenciadorDeAlunos(nome_arquivo)
    
    # Pergunta ao usuário qual chave deseja usar para a ordenação
    print("Escolha a chave para ordenação:")
    print("1. Nome")
    print("2. Matrícula")
    print("3. Curso")
    opcao_chave = int(input("Escolha uma opção (1-3): "))
    
    if opcao_chave == 1:
        chave = "nome"
    elif opcao_chave == 2:
        chave = "matricula"
    elif opcao_chave == 3:
        chave = "curso"
    
    # Pergunta ao usuário o nome do arquivo de saída
    nome_arquivo_saida = input("Digite o nome do arquivo de saída (sem a extensão): ")
    
    # Dictionary to store execution times
    tempos = {}
    
    # Create and start threads for each sorting method
    threads = []
    for metodo in ["sort", "bolha", "selecao", "insercao"]:
        thread = threading.Thread(target=executar_ordenacao, args=(gerenciador, chave, metodo, nome_arquivo_saida, tempos))
        thread.start()
        threads.append(thread)
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    
    # Print execution times
    for metodo, tempo in tempos.items():
        print(f"Tempo de execução para {metodo}: {tempo} segundos")
    
    # Determine the sorting method with the shortest execution time
    metodo_mais_agil = min(tempos, key=tempos.get)
    print(f"O método mais ágil foi: {metodo_mais_agil}")

if __name__ == "__main__":
    main()