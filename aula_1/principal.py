# Abrir o arquivo para leitura
with open('/var/www/html/Pesquisa_ordenação/aula_1/dados.txt', 'r') as arquivo:
    # Ler os dados do arquivo e armazená-los em um vetor
    vetor = [int(numero) for numero in arquivo.readlines()]

# Ordenar o vetor
vetor.sort()

# Imprimir o vetor ordenado
print(vetor)