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
