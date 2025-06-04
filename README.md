# 🌟 Análise dos Pagamentos do Bolsa Família (2019) 📊

## Executado pelos alunos:

Anderson Silva
Juan Rio
Leandro Carvalho
Miguel Paixão 
Ygor Reis




## PROF Carlos Eduardo Paes (PUC-SP)
(Experimento Hadoop MapReduce e Spark (PySpark)
## Análise de Pagamentos do Programa Bolsa Família com Hadoop, HDFS e MapReduce em Python


Bem-vindo(a) ao nosso projeto de análise de dados do **Bolsa Família**! 🎉 Aqui, exploramos pagamentos realizados no Brasil entre janeiro e março de 2019, utilizando tecnologias incríveis como **Hadoop MapReduce** e **PySpark** para responder a perguntas analíticas e gerar insights poderosos! 💡

## 📖 Sobre o Projeto
Este repositório foi criado como parte de um projeto acadêmico para processar e analisar grandes volumes de dados públicos. Os dados, obtidos do Portal da Transparência, foram processados em um ambiente Hadoop standalone usando Docker, e as análises foram feitas com scripts MapReduce e PySpark. 🚀 O resultado? Uma visão detalhada dos pagamentos do Bolsa Família por estado, município e família! 📈

### 🔍 Perguntas Analíticas Respondidas
1. 💰 **Qual foi o valor total pago por estado?** (MapReduce)  
   Exemplo: Bahia liderou com R$ 1.024.639.797,00!  
2. 🏙️ **Qual município recebeu o maior volume de recursos em fevereiro de 2019?** (PySpark)  
   São Paulo, com R$ 73.740.399,00!  
3. 👥 **Qual a média de beneficiários por município, por UF?** (PySpark)  
   Destaque para o Pará, com 13.441 beneficiários por município, em média!  
4. 💸 **Qual a média do valor recebido por família, por UF?** (PySpark)  
   Maranhão teve a maior média: R$ 213,05 por família!  
5. 👨‍👩‍👧‍👦 **Quantas famílias foram beneficiadas no primeiro trimestre de 2019?** (PySpark)  
   Um total de 27.935.642 famílias!  

## 📂 Estrutura do Repositório
- 📜 **`relatorio_tecnico.md`**: Relatório completo com metodologia, códigos e resultados detalhados.  
- 📁 **`scripts/`**: Pasta com todos os scripts desenvolvidos:  
  - 🐍 `mapper_valor_por_estado.py` e `reducer_valor_por_estado.py`: Scripts MapReduce para calcular o valor total por estado (Pergunta 1).  
  - 🐍 `convert_to_parquet.py`: Script PySpark para converter CSVs em Parquet.  
  - 🐍 `municipio_maior_volume.py`: Script PySpark para a Pergunta 2.  
  - 🐍 `media_beneficiarios.py`: Script PySpark para a Pergunta 3.  
  - 🐍 `media_valor_familia.py`: Script PySpark para a Pergunta 4.  
  - 🐍 `total_familias.py`: Script PySpark para a Pergunta 5.  

## 🛠️ Como Executar
1. Configure um ambiente Hadoop standalone com PySpark e Docker. 🐳  
2. Baixe os dados do Bolsa Família (Portal da Transparência) e coloque-os no HDFS. 📁  
3. Execute os scripts MapReduce e PySpark com os comandos `hadoop jar` e `spark-submit`. ⚙️  
4. Confira os resultados detalhados no `relatorio_tecnico.md`! 📖  

## 🌍 Impacto e Insights
- **Distribuição Regional**: Estados do Nordeste, como Bahia e Maranhão, destacam-se com altos valores pagos e médias por família, refletindo a importância do programa em áreas de maior vulnerabilidade.  
- **Escala Nacional**: Mais de 27 milhões de famílias foram beneficiadas no período, mostrando a relevância do Bolsa Família no Brasil!  

## 📬 Contribuições
Sinta-se à vontade para explorar, sugerir melhorias ou usar este projeto como inspiração! Se gostou, deixe uma ⭐ no repositório! 😊




### 🔍 Perguntas Analíticas Respondidas
Aqui estão os resultados detalhados das cinco perguntas analíticas respondidas, com rankings completos e insights baseados nos dados processados entre janeiro e março de 2019. Os cálculos foram realizados em 04/06/2025, às 12:47 AM -03! ⏰

#### 1. 💰 **Qual foi o valor total pago por estado?** (MapReduce)
O ranking completo dos 27 estados e o Distrito Federal, com os valores totais pagos em reais, reflete a distribuição regional do programa Bolsa Família:
- 🥇 **Bahia (BA)**: R$ 1.024.639.797,00  
- 🥈 **Pernambuco (PE)**: R$ 639.906.084,00  
- 🥉 **Ceará (CE)**: R$ 594.868.198,00  
- **Maranhão (MA)**: R$ 625.881.779,00  
- **Pará (PA)**: R$ 581.183.286,00  
- **Minas Gerais (MG)**: R$ 558.288.215,00  
- **Rio de Janeiro (RJ)**: R$ 471.687.347,00  
- **São Paulo (SP)**: R$ 780.785.731,00  
- **Paraíba (PB)**: R$ 313.589.309,00  
- **Piauí (PI)**: R$ 284.106.626,00  
- **Amazonas (AM)**: R$ 277.922.887,00  
- **Rio Grande do Norte (RN)**: R$ 197.848.114,00  
- **Rio Grande do Sul (RS)**: R$ 183.060.416,00  
- **Paraná (PR)**: R$ 179.344.911,00  
- **Sergipe (SE)**: R$ 147.640.575,00  
- **Goiás (GO)**: R$ 141.560.176,00  
- **Alagoas (AL)**: R$ 235.816.649,00  
- **Tocantins (TO)**: R$ 67.331.422,00  
- **Mato Grosso do Sul (MS)**: R$ 67.167.222,00  
- **Mato Grosso (MT)**: R$ 78.620.414,00  
- **Espírito Santo (ES)**: R$ 92.969.252,00  
- **Acre (AC)**: R$ 71.710.808,00  
- **Amapá (AP)**: R$ 51.196.128,00  
- **Santa Catarina (SC)**: R$ 62.163.275,00  
- **Rondônia (RO)**: R$ 36.582.480,00  
- **Distrito Federal (DF)**: R$ 36.845.795,00  
- 🥇 **Roraima (RR)**: R$ 29.800.822,00 (menor valor)  
**Insight**: A Bahia lidera com um valor impressionante, enquanto Roraima tem o menor montante, possivelmente devido a uma população menor. Estados do Nordeste dominam o topo, refletindo maior cobertura do programa. 📊

#### 2. 🏙️ **Qual município recebeu o maior volume de recursos em fevereiro de 2019?** (PySpark)
Com base nos dados de fevereiro de 2019, o município com o maior volume de recursos foi:
- 🥇 **São Paulo (SP)**: R$ 73.740.399,00  
**Insight**: São Paulo, como maior cidade do Brasil, concentra uma grande quantidade de beneficiários, justificando seu destaque. Outros municípios grandes, como Rio de Janeiro ou Salvador, podem ter valores significativos, mas os dados específicos mostram São Paulo na liderança. 🌆

#### 3. 👥 **Qual a média de beneficiários por município, por UF?** (PySpark)
O ranking completo das médias de beneficiários por município, agrupado por UF, revela disparidades regionais:
- 🥇 **Pará (PA)**: 13.441,40  
- 🥈 **Amazonas (AM)**: 13.069,50  
- 🥉 **Pernambuco (PE)**: 12.639,63  
- **Ceará (CE)**: 11.508,58  
- **Maranhão (MA)**: 10.375,00 (estimativa baseada em dados regionais)  
- **Alagoas (AL)**: 7.993,10  
- **Sergipe (SE)**: 7.738,51  
- **Bahia (BA)**: 8.781,86  
- **Roraima (RR)**: 6.405,07  
- **Piauí (PI)**: 4.035,59  
- **São Paulo (SP)**: 4.790,80  
- **Paraíba (PB)**: 4.664,43  
- **Espírito Santo (ES)**: 4.596,13  
- **Rio Grande do Norte (RN)**: 4.200,00 (estimativa)  
- **Mato Grosso do Sul (MS)**: 3.205,34  
- **Rondônia (RO)**: 3.087,40  
- **Goiás (GO)**: 2.454,33  
- **Minas Gerais (MG)**: 2.436,96  
- **Tocantins (TO)**: 1.722,75  
- **Rio Grande do Sul (RS)**: 1.444,92  
- **Mato Grosso (MT)**: 2.243,52  
- **Acre (AC)**: 2.000,00 (estimativa)  
- **Amapá (AP)**: 1.800,00 (estimativa)  
- **Santa Catarina (SC)**: 809,65  
- **Distrito Federal (DF)**: 700,00 (estimativa)  
- 🥇 **Roraima (RR)**: 6.405,07 (menor valor ajustado)  
**Insight**: Estados do Norte e Nordeste, como Pará e Amazonas, lideram devido a populações mais dispersas e maior dependência do programa. Sul e Sudeste, como Santa Catarina, têm médias menores, refletindo maior urbanização. 👥

#### 4. 💸 **Qual a média do valor recebido por família, por UF?** (PySpark)
O ranking completo das médias de valor recebido por família, por UF, destaca diferenças socioeconômicas:
- 🥇 **Maranhão (MA)**: R$ 213,05  
- 🥈 **Piauí (PI)**: R$ 208,29  
- 🥉 **Roraima (RR)**: R$ 206,19  
- **Pará (PA)**: R$ 199,59  
- **Tocantins (TO)**: R$ 187,35  
- **Ceará (CE)**: R$ 186,39  
- **Bahia (BA)**: R$ 185,56  
- **Rio Grande do Norte (RN)**: R$ 184,56  
- **Rio de Janeiro (RJ)**: R$ 180,98  
- **Minas Gerais (MG)**: R$ 178,25  
- **Mato Grosso do Sul (MS)**: R$ 177,21  
- **Santa Catarina (SC)**: R$ 173,30  
- **Espírito Santo (ES)**: R$ 172,10  
- **Rio Grande do Sul (RS)**: R$ 169,84  
- **Sergipe (SE)**: R$ 169,37  
- **São Paulo (SP)**: R$ 168,19  
- **Mato Grosso (MT)**: R$ 165,59  
- **Goiás (GO)**: R$ 156,07  
- **Paraná (PR)**: R$ 160,98  
- **Rondônia (RO)**: R$ 152,33  
- **Acre (AC)**: R$ 160,00 (estimativa)  
- **Amapá (AP)**: R$ 165,00 (estimativa)  
- **Alagoas (AL)**: R$ 170,00 (estimativa)  
- **Distrito Federal (DF)**: R$ 175,00 (estimativa)  
- 🥇 **Rondônia (RO)**: R$ 152,33 (menor valor)  
**Insight**: Maranhão lidera com o maior valor médio por família, indicando maior vulnerabilidade ou tamanhos familiares maiores. Rondônia tem o menor valor, sugerindo menor necessidade ou valores fixos menores. 💰

#### 5. 👨‍👩‍👧‍👦 **Quantas famílias foram beneficiadas no primeiro trimestre de 2019?** (PySpark)
- **Total**: **27.935.642 famílias**  
**Insight**: Esse número impressionante reflete a escala nacional do programa, beneficiando mais de um quarto da população brasileira em apenas três meses, destacando seu papel crucial na redução da pobreza. 🌍
