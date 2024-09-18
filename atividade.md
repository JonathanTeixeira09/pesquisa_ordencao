
# Avaliação semestral de Pesquisa e Ordenação
# 18/09/24
# Nome: JOnathan Teixeira

## 1. O que é ordenação e qual o seu papel nos sistemas de informação?

Ordenação é o processo de reorganizar elementos de uma lista ou vetor em uma sequência específica, normalmente em ordem crescente ou decrescente. Nos sistemas de informação, a ordenação é essencial para a eficiência na busca, manipulação e exibição de dados. Em sistemas que lidam com grandes volumes de dados, a ordenação facilita operações como busca binária, que depende de uma lista ordenada para funcionar, e também otimiza o uso de memória e processamento.

## 2. Como se calcula ou se mede a complexidade nos algoritmos de ordenação?

A complexidade de um algoritmo de ordenação é medida em termos de tempo e espaço, geralmente expressa em O-notation (notação Big-O), que descreve o comportamento do tempo de execução ou o uso de memória em função do tamanho da entrada (n). Para calcular a complexidade, analisamos o número de comparações e trocas que o algoritmo faz à medida que o tamanho da lista aumenta.

- Melhor caso: Quando a entrada já está ordenada.
- Pior caso: Quando a entrada está na ordem inversa.
- Caso médio: Representa o desempenho típico do algoritmo.

## 3. O que significa um algoritmo ser estável ou instável na ordenação?

Um algoritmo de ordenação é considerado estável se ele mantém a ordem relativa dos elementos com chaves iguais. Ou seja, se dois elementos possuem o mesmo valor e aparecem em uma certa ordem antes da ordenação, eles devem manter essa ordem após a ordenação. 
- Algoritmos estáveis garantem que se dois registros A e B têm a mesma chave, mas A aparece antes de B na lista original, essa ordem será mantida após a ordenação.
- Algoritmos instáveis podem não preservar essa ordem relativa.

## 4. Qual dos algoritmos estudados (bolha, seleção, inserção e pente) tem o desempenho muito bom? Qual recurso ele utiliza?

O algoritmo inserção tende a ter o melhor desempenho em listas pequenas ou quase ordenadas, pois faz menos comparações e trocas quando a lista já está próxima da ordenação correta. Ele utiliza a técnica de inserção direta, onde elementos são movidos para suas posições corretas à medida que são encontrados, resultando em menos operações desnecessárias em listas quase ordenadas. Isso o torna muito eficiente no melhor caso, que tem complexidade O(n).

## 5. Analisando a sequência:
Índices:  0 1 2 3 4 5 6  
Valores:  7 3 5 1 8 2 5

### A) Quantas comparações e trocas no Bolha?
- Primeira passada: 6 comparações, 4 trocas
- Segunda passada: 5 comparações, 3 trocas
- Terceira passada: 4 comparações, 2 trocas
- Quarta passada: 3 comparações, 1 troca
- Quinta passada: 2 comparações, 0 trocas

Total: **20 comparações e 10 trocas**

### B) Quantas comparações e trocas no Pente?
- Primeira passada (gap de 4): 3 comparações e 2 trocas
- Segunda passada (gap de 3): 4 comparações e 2 trocas
- Terceira passada (gap de 2): 5 comparações e 3 trocas
- Última passada (gap de 1, igual ao Bubble Sort): 6 comparações e 2 trocas

Total: **18 comparações e 9 trocas**.

## 6. Quais algoritmos são estáveis e quais são instáveis?

- **Estáveis**: Bolha (Bubble Sort), Inserção (Insertion Sort)
- **Instáveis**: Seleção (Selection Sort), Pente (Comb Sort)

## 7. Alterações na classe Pessoa para usar o método sort() em Java ou C#

Em Java e C#, para que o método sort() funcione corretamente com objetos da classe Pessoa, é necessário implementar a interface Comparable ou definir um Comparator específico.

### Exemplo em Java:

```java
public class Pessoa implements Comparable<Pessoa> {
   private String nome;
   private String curso;

   public Pessoa(String nome, String curso) {
       this.nome = nome;
       this.curso = curso;
   }

   @Override
   public int compareTo(Pessoa outra) {
       int nomeComparison = this.nome.compareTo(outra.nome);
       if (nomeComparison != 0) {
           return nomeComparison;
       }
       return this.curso.compareTo(outra.curso);
   }
}
```

Neste exemplo, a classe Pessoa implementa o método compareTo(), que primeiro compara os nomes e, se os nomes forem iguais, compara os cursos. Isso garante que a ordenação aconteça de forma correta considerando esses dois atributos.