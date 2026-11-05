# Atividade - Analise de algoritmos de ordenacao

## O que foi feito
Comparei Bubble Sort, Insertion Sort, Selection Sort e Quick Sort usando vetores com 10, 20 e 1.000 numeros.

## Como executar
1. Baixe o arquivo `atividade.py`.
2. Execute com Python 3:
   `python atividade.py`

## Como contei
- Comparacoes: cada verificacao entre dois valores.
- Bubble, Selection e Quick: cada troca real entre duas posicoes.
- Insertion: cada escrita no vetor, incluindo deslocamentos e a colocacao da chave.

## Resultados do teste principal

Os valores abaixo mostram comparacoes / trocas ou movimentacoes.

| Tamanho | Bubble | Insertion | Selection | Quick |
|---|---:|---:|---:|---:|
| 10 | 44 / 19 | 27 / 28 | 45 / 7 | 29 / 7 |
| 20 | 189 / 84 | 99 / 103 | 190 / 16 | 58 / 28 |
| 1.000 | 499.122 / 239.681 | 240.670 / 240.680 | 499.500 / 992 | 10.385 / 4.543 |

## Respostas

**a)** Insertion Sort fez menos comparacoes para 10 elementos.

**b)** Selection Sort e Quick Sort fizeram menos trocas: 7 cada.

**c)** Nao. Os resultados mudaram quando aumentou a quantidade de numeros.

**d)** As operacoes aumentaram bastante, principalmente nos algoritmos mais simples.

**e)** Nao. Mesmo tendo complexidade O(n²), cada algoritmo fez uma quantidade diferente de operacoes.

**f)** O Bubble Sort teve muitas movimentacoes. Em comparacoes, Selection ficou um pouco acima.

**g)** O Quick Sort teve o melhor resultado com 1.000 numeros.

**h)** Sim, os resultados ficaram de acordo com a teoria estudada.

**i)** Eu escolheria o Quick Sort, porque realizou menos operacoes no teste maior.

## Desafio adicional

O programa tambem testa um vetor aleatorio, um ordenado e um invertido, todos com 1.000 elementos.

**Conclusao:** A organizacao dos numeros muda os resultados. Bubble e Insertion trabalham melhor quando os numeros ja estao ordenados. Selection mantem a mesma quantidade de comparacoes. O Quick Sort pode ter um resultado ruim dependendo da escolha do pivo.
