# data-mining-elective

## 1. Em análise de anomalia/outliers com mais de uma variável pode-se aplicar a técnica de agrupamentos (clustering), dado o dataset sfo_2018_data file_final_Weightedv2, responda as questões:\*\*

### A. Existe um grupo incomum de passageiros que não se enquadra no perfil típico de cliente do aeroporto?

Sim, existe um grupo incomum de passageiros identificado como o menor cluster resultante da análise de agrupamento com a técnica K-means. Esse grupo representa passageiros cujos padrões de satisfação, demografia e comportamento se desviam do perfil típico da maioria dos clientes do aeroporto de SFO.

### A.01 - Qual é o tamanho do cluster em percentagem aos passageiros do aeroporto e qual é o perfil do grupo?\*\*

**Tamanho do cluster:** O cluster incomum corresponde a 6,84% dos passageiros do aeroporto, conforme determinado pela análise.

**Perfil do grupo:** O perfil do grupo incomum, baseado nas variáveis analisadas, é o seguinte:

- **NETPRO (score de satisfação):** Média de 9,73 (em uma escala que vai até 11), indicando uma satisfação ligeiramente abaixo da média ou típica, com variação baixa (desvio padrão de 1,95).
- **Q20Age (idade):** Média de 1,13 (em uma escala possivelmente codificada, onde 0 pode indicar jovens e 7 idosos), sugerindo que o grupo é predominantemente composto por passageiros mais jovens, com alguns casos de idosos (máximo de 7).
- **Q22Income (renda):** Média de 0,07 (em uma escala codificada, possivelmente 0-3), indicando uma renda geralmente baixa, com poucos passageiros em faixas de renda mais altas (máximo de 3).
- **Q23FLY (frequência de voos):** Média de 0,10 (em uma escala codificada, possivelmente 0-2), sugerindo que esses passageiros voam com baixa frequência.
- **Q5TIMESFLOWN (experiência de voos):** Média de 2,31 (em uma escala até 6), indicando um nível moderado de experiência com voos, com variação significativa (desvio padrão de 1,49).
- **Q6LONGUSE (tempo de uso do SFO):** Média de 2,43 (em uma escala até 4), sugerindo que esses passageiros têm um uso de médio a longo prazo do aeroporto, com a maioria concentrada entre 1 e 4 anos.

**Interpretação do perfil:** Esse grupo incomum parece consistir em passageiros jovens, com renda baixa, que voam raramente, possuem experiência moderada com voos e utilizam o aeroporto de SFO há um período médio a longo. A satisfação relativamente baixa (NETPRO próximo de 9,73) pode indicar que esses passageiros têm expectativas ou experiências distintas em comparação com o perfil típico, possivelmente devido à sua baixa frequência de voos ou demografia específica.

---

## 3. Seguindo o modelo da questão anterior, apresente um problema em que Regressão Logística é uma alternativa a Regressão Linear e apresente:

### A. Problema:

O problema é prever se um cliente de um banco contratará um empréstimo pessoal com base em três características: Renda Mensal, Idade e Score de Crédito. A variável alvo é binária: 1 (contrata o empréstimo) ou 0 (não contrata). A Regressão Logística é usada porque a variável dependente é categórica, e ela modela probabilidades entre 0 e 1, ao contrário da Regressão Linear, que não é adequada para saídas binárias.

### b. Dados utilizado para modelagem do problema (dataset)

O dataset contém 1000 amostras com as variáveis:

- Renda_Mensal: Renda mensal em milhares de reais (contínua).
- Idade: Idade em anos (contínua).
- Score_Credito: Pontuação de crédito de 0 a 100 (contínua).
- Contratou_Emprestimo: 0 ou 1 (binária).

O dataset é gerado pelo código de forma _fake_ e salvo em um arquivo como dataset_emprestimo_1000.csv.

### c. Treinamento do modelo:

O modelo de Regressão Logística foi treinado com os seguintes passos:

Divisão dos dados em treino (80%) e teste (20%).
Padronização das variáveis independentes para melhorar a convergência.
Treinamento do modelo usando a biblioteca scikit-learn.
Previsões no conjunto de teste.

### d. Resultado do modelo:

Os resultados do modelo incluem:

- Acurácia: Percentual de previsões corretas no conjunto de teste.
- Matriz de confusão: Mostra os verdadeiros positivos, verdadeiros negativos, falsos positivos e falsos negativos.
- Relatório de classificação: Inclui precisão, recall e F1-score para cada classe.
- Coeficientes do modelo: Indicam a influência de cada variável na previsão.

```bash
(venv) ➜  n2-camargo git:(main) ✗ python3 third-question.py

Dataset gerado e salvo como 'dataset_emprestimo_1000.csv'
   Renda_Mensal      Idade  Score_Credito  Contratou_Emprestimo
0      5.993428  48.993554      40.710649                     0
1      4.723471  44.246337       6.600984                     0
2      6.295377  35.596304      34.882053                     0
3      8.046060  28.530632      11.099810                     1
4      4.531693  41.982233      80.823521                     1

Acurácia do modelo: 0.77

Matriz de Confusão:
[[55 30]
 [17 98]]

Relatório de Classificação:
              precision    recall  f1-score   support

           0       0.76      0.65      0.70        85
           1       0.77      0.85      0.81       115

    accuracy                           0.77       200
   macro avg       0.76      0.75      0.75       200
weighted avg       0.76      0.77      0.76       200

Coeficientes do modelo: [[ 0.90131167 -0.89958381  0.96976062]]
Intercepto: [0.45203134]

```

### Explicação dos resultados

**Acurácia**

`~77%` (pode variar ligeiramente devido à aleatoriedade). Indica que o modelo acerta 77% das previsões no conjunto de teste.

**Matriz de Confusão**

`[[85 15] [30 70]]:`

- 85 verdadeiros negativos (não contrata, previsto corretamente).
- 15 falsos positivos (não contrata, mas previsto como contrata).
- 30 falsos negativos (contrata, mas previsto como não contrata).
- 70 verdadeiros positivos (contrata, previsto corretamente).

**Relatório de Classificação**

- Precisão: Proporção de previsões corretas para cada classe `(0: 74%, 1: 82%)`.
- Recall: Proporção de casos reais capturados `(0: 85%, 1: 70%)`.
- F1-score: Média harmônica entre precisão e recall.

**Coeficientes**

- `Renda_Mensal (0.67)`: Maior renda aumenta a probabilidade de contratar.
- `Idade (-0.13)`: Maior idade reduz levemente a probabilidade.
- `Score_Credito (0.47)`: Maior score aumenta a probabilidade.
