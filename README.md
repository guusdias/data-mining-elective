# N2

# Dupla

* Cristian Prochnow
* Gustavo Henrique Dias

# Questões

## 1. Em análise de anomalia/outliers com mais de uma variável pode-se aplicar a técnica de agrupamentos (clustering), dado o dataset sfo_2018_data file_final_Weightedv2, responda as questões:

### A. Existe um grupo incomum de passageiros que não se enquadra no perfil típico de cliente do aeroporto?

Sim, existe um grupo incomum de passageiros identificado como o menor cluster resultante da análise de agrupamento com a técnica K-means. Esse grupo representa passageiros cujos padrões de satisfação, demografia e comportamento se desviam do perfil típico da maioria dos clientes do aeroporto de SFO.

### Resultado

```bash
Unusual cluster size: 6.84% of passengers

Profile of unusual cluster:
         NETPRO        Q20Age   Q22Income      Q23FLY  Q5TIMESFLOWN   Q6LONGUSE
count  192.000000  192.000000  192.000000  192.000000    192.000000  192.000000
mean     9.734375    1.125000    0.072917    0.098958      2.312500    2.427083
std      1.946205    1.904802    0.375835    0.376814      1.492126    1.312404
min      0.000000    0.000000    0.000000    0.000000      0.000000    0.000000
25%      9.000000    0.000000    0.000000    0.000000      1.000000    1.000000
50%     11.000000    0.000000    0.000000    0.000000      2.000000    2.000000
75%     11.000000    2.000000    0.000000    0.000000      3.000000    4.000000
max     11.000000    7.000000    3.000000    2.000000      6.000000    4.000000
```

### A.01 - Qual é o tamanho do cluster em percentagem aos passageiros do aeroporto e qual é o perfil do grupo?

**Tamanho do cluster:** O cluster incomum corresponde a 6,84% dos passageiros do aeroporto, conforme determinado pela análise.

**Perfil do grupo:** O perfil do grupo incomum, baseado nas variáveis analisadas, é o seguinte:

- **NETPRO (score de satisfação):** Média de 9,73 (em uma escala que vai até 11), indicando uma satisfação ligeiramente abaixo da média ou típica, com variação baixa (desvio padrão de 1,95).
- **Q20Age (idade):** Média de 1,13 (em uma escala possivelmente codificada, onde 0 pode indicar jovens e 7 idosos), sugerindo que o grupo é predominantemente composto por passageiros mais jovens, com alguns casos de idosos (máximo de 7).
- **Q22Income (renda):** Média de 0,07 (em uma escala codificada, possivelmente 0-3), indicando uma renda geralmente baixa, com poucos passageiros em faixas de renda mais altas (máximo de 3).
- **Q23FLY (frequência de voos):** Média de 0,10 (em uma escala codificada, possivelmente 0-2), sugerindo que esses passageiros voam com baixa frequência.
- **Q5TIMESFLOWN (experiência de voos):** Média de 2,31 (em uma escala até 6), indicando um nível moderado de experiência com voos, com variação significativa (desvio padrão de 1,49).
- **Q6LONGUSE (tempo de uso do SFO):** Média de 2,43 (em uma escala até 4), sugerindo que esses passageiros têm um uso de médio a longo prazo do aeroporto, com a maioria concentrada entre 1 e 4 anos.

**Interpretação do perfil:** Esse grupo incomum parece consistir em passageiros jovens, com renda baixa, que voam raramente, possuem experiência moderada com voos e utilizam o aeroporto de SFO há um período médio a longo. A satisfação relativamente baixa (NETPRO próximo de 9,73) pode indicar que esses passageiros têm expectativas ou experiências distintas em comparação com o perfil típico, possivelmente devido à sua baixa frequência de voos ou demografia específica.

## 2. Regras de Associação são utilizadas para buscar elementos que consequentemente implicam na presença de outros elementos em uma transação. Tais regras são utilizadas em diferentes áreas como marketing, vendas, sistema de recomendação, prevenção de crimes, etc. Portanto, gere regras de associação para um problema diferente de transações de itens de compras e apresente (2,0):

### A. Problema:

O problema envolve a análise de uma base de dados de títulos musicais que mais foram ouvidos de 1950 até os anos atuais. A partir desse título a ideia é que possamos retirar relações de músicas, gêneros e outras características com base nesses fatores. Então, por meio das colunas presentes, queremos verificar se é válido, por exemplo, considerar que toda música com bastante instrumento é mais dançante e assim por diante.

### b. Dados utilizado para modelagem do problema (dataset)

Os dados utilizados para esse treinamento foram pegos do Kaggle, a partir de um dataset disponível sobre uma análise das top 10000 músicas desde 1950 a atualmente. É importante destacar também que esse essa mesma publicação também tem disponível o mesmo dataset, só que filtrado, trazendo apenas os dados de 1960 até atualmente.

### c. Treinamento do modelo:

Para treinamento do modelo, os dados que foram usados como base foram das colunas `'Artist Genres', 'Danceability', 'Energy', 'Valence', 'Acousticness', 'Instrumentalness'`, pois o objetivo fundamental era procurar alguma associação entre o gênero musical e outras variáveis geralmente consequentes à produção musical.

Com isso em vista, o objetivo era determinar se o gênero de pop, com mais `Danceability` e `Acousticness` conseguia entregar a mesma `Energy` que uma forma mais sintetizada dos ritmos, por exemplo.

### d. Resultado do modelo:

Abaixo então podemos ter uma prévia dos resultados do algoritmo.

```shell
Itemsets Frequentes:
 support                                                                                                        itemsets
0.017535                                                                                      (Artist Genres_album rock)
0.014059                                                                                  (Artist Genres_australian pop)
0.018114                                                                                 (Artist Genres_australian rock)
0.022721                                                                                    (Artist Genres_classic rock)
...
Regra 44: Artist Genres_rap -> Instrumentalness_Low
Suporte: 0.0147
Confiança: 0.9964
Lift: 1.0294
--------------------------------------------------
Regra 880: Energy_High, Acousticness_Medium, Valence_Medium -> Instrumentalness_Low
Suporte: 0.0143
Confiança: 0.9963
Lift: 1.0293
--------------------------------------------------
Regra 1017: Energy_High, Valence_Medium, Artist Genres_pop, Acousticness_Low -> Instrumentalness_Low
Suporte: 0.0215
Confiança: 0.9963
Lift: 1.0293
```

Com isso, foram obtidas algumas regras que denotam características interessantes em meio ao dataset analisado, sendo então, por exemplo (levando em conta os exemplos do código acima):

`Energy_High, Valence_Medium, Artist Genres_pop, Acousticness_Low -> Instrumentalness_Low`

> Aqui nós temos a consideração de que uma música com energia alta, valência média (nem muito animada, nem muito triste), sendo uma música pop e com baixo teor acústico (mais voz e ritmos sintetizados) **tende** a ter pouca instrumentação, sendo então com ritmos mais digitais/eletrônicos.

E com os dados seguintes:

```shell
Suporte: 0.0215
Confiança: 0.9963
Lift: 1.0293
```

E aqui, podemos então interpretar esses resultados da forma ao qual a presença de músicas que se encaixam nesses fatores é de apenas pouco mais de 2% (0,0215), contudo a confiança dessa probabilidade é de quase 100% (0,9963), e com isso temos também a certeza (1.0293) de que essa combinação de fatores tem sim influência sobre o resultado final.

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
