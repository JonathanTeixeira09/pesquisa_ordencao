import random
import string

class GeradorDeNomes:
    def __init__(self):
        self.num_nomes = 0
        self.num_caracteres = 0
        self.nomes = []

    def solicitar_quantidade(self):
        self.num_nomes = int(input("Quantos nomes você deseja criar? "))

    def solicitar_tamanho(self):
        self.num_caracteres = int(input("Com quantos caracteres cada nome deve ter? "))

    def gerar_nomes(self):
        self.nomes = []
        for _ in range(self.num_nomes):
            nome = ''.join(random.choices(string.ascii_letters, k=self.num_caracteres))
            self.nomes.append(nome)

    def gerar_arquivo(self):
        resposta = input("Deseja gerar um arquivo com os nomes gerados? (S/N) ")
        if resposta.lower() == 's':
            with open('nomes.txt', 'w') as arquivo:
                for nome in self.nomes:
                    arquivo.write(nome + '\n')
            print("Arquivo 'nomes.txt' gerado com sucesso!")

    def ordenar_nomes(self):
        resposta = input("Deseja ordenar os nomes gerados? (S/N) ")
        if resposta.lower() == 's':
            self.nomes.sort()
            print("Nomes ordenados:")
            for nome in self.nomes:
                print(nome)
        else:
            print("Nomes não ordenados:")
            for nome in self.nomes:
                print(nome)

    def executar(self):
        self.solicitar_quantidade()
        self.solicitar_tamanho()
        self.gerar_nomes()
        self.gerar_arquivo()
        self.ordenar_nomes()

gerador = GeradorDeNomes()
gerador.executar()