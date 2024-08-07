import random

class Numeros:
    @staticmethod
    def popular_aleatorio(lista, n, limite):
        lista.append(random.randint(0, limite))

def ordenar_numeros():
    # Abrir o arquivo
    with open('/var/www/html/Pesquisa_ordenação/aula_1/numeros.txt', 'r') as arquivo:
        # Ler os dados do arquivo
        dados = arquivo.readlines()
        
        # Armazenar os números em um vetor
        numeros = [int(numero) for numero in dados]
        
        # Ordenar os números
        numeros.sort()
        
        # Imprimir os números ordenados
        for numero in numeros:
            print(numero)

# Chamar a função para ordenar os números
ordenar_numeros()