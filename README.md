![Bolsa Família Analysis](https://via.placeholder.com/800x200.png?text=Análise+Bolsa+Família+2019)
# 🌟 Análise dos Pagamentos do Bolsa Família (2019) 📊

Bem-vindo(a) ao meu projeto de análise de dados do **Bolsa Família**! 🎉 Aqui, explorei os pagamentos realizados no Brasil entre janeiro e março de 2019, utilizando tecnologias incríveis como **Hadoop MapReduce** e **PySpark** para responder a perguntas analíticas e gerar insights poderosos! 💡


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

## 🧑‍💻 Sobre Mim
Sou um estudante apaixonado por dados e tecnologia, e este projeto foi uma oportunidade incrível para aprender mais sobre Big Data e análise de dados públicos! Conecte-se comigo no [LinkedIn](#) ou envie um e-mail para [seu-email@exemplo.com]! 📧
