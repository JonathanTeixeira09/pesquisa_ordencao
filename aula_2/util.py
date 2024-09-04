import random
import string

class GeradorDeDados:
    
    """## gerar_numeros
    Método que gera números aleatórios com base na quantidade de elementos e no tamanho de cada elemento.
    """
    """## gerar_letras
    Método que gera letras aleatórias com base na quantidade de elementos e no tamanho de cada elemento.
    """
    """## gerar_arquivo
    Método que gera um arquivo com os dados gerados.
    """
    """## ordenar_dados
    Método que ordena os dados gerados.
    """
    """## executar
    Método que executa o programa.
    """
    
    def __init__(self):
        self.num_elementos = 0
        self.num_caracteres = 0
        self.dados = []

    def solicitar_quantidade(self):
        self.num_elementos = int(input("Quantos elementos você deseja criar? "))

    def solicitar_tamanho(self):
        self.num_caracteres = int(input("Com quantos caracteres cada elemento deve ter? "))

    def solicitar_tipo(self):
        tipo = input("Qual tipo de elemento você deseja gerar? (N - Números, L - Letras) ").lower()
        if tipo == 'n':
            self.gerar_numeros()
        elif tipo == 'l':
            self.gerar_letras()
        else:
            print("Tipo inválido!")

    def gerar_numeros(self):
        self.dados = []
        for _ in range(self.num_elementos):
            numero = ''.join(random.choices(string.digits, k=self.num_caracteres))
            self.dados.append(numero)

    def gerar_letras(self):
        self.dados = []
        for _ in range(self.num_elementos):
            nome = ''.join(random.choices(string.ascii_letters, k=self.num_caracteres))
            self.dados.append(nome)

    def gerar_arquivo(self):
        resposta = input("Deseja gerar um arquivo com os dados gerados? (S/N) ")
        if resposta.lower() == 's':
            with open('dados.txt', 'w') as arquivo:
                for dado in self.dados:
                    arquivo.write(dado + '\n')
            print("Arquivo 'dados.txt' gerado com sucesso!")

    def ordenar_dados(self):
        resposta = input("Deseja ordenar os dados gerados? (S/N) ")
        if resposta.lower() == 's':
            self.dados.sort()
            print("Dados ordenados:")
            for dado in self.dados:
                print(dado)
        else:
            print("Dados não ordenados:")
            for dado in self.dados:
                print(dado)

    def executar(self):
        self.solicitar_quantidade()
        self.solicitar_tamanho()
        self.solicitar_tipo()
        self.gerar_arquivo()
        self.ordenar_dados()

