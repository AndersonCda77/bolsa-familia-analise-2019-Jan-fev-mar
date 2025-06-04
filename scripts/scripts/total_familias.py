from pyspark.sql import SparkSession
from pyspark.sql.functions import col, countDistinct
from pyspark.sql.types import StructType, StructField, StringType, LongType, DoubleType

schema = StructType([
    StructField("MÊS COMPETÊNCIA", LongType(), True),
    StructField("MÊS REFERÊNCIA", LongType(), True),
    StructField("UF", StringType(), True),
    StructField("CÓDIGO MUNICÍPIO SIAFI", LongType(), True),
    StructField("NOME MUNICÍPIO", StringType(), True),
    StructField("CPF FAVORECIDO", StringType(), True),
    StructField("NIS FAVORECIDO", StringType(), True),
    StructField("NOME FAVORECIDO", StringType(), True),
    StructField("VALOR PARCELA", DoubleType(), True)
])

spark = SparkSession.builder.appName("TotalFamilias").getOrCreate()

df = spark.read.schema(schema).parquet("/user/dados/bolsa-familia/parquet/*.parquet")
print("Total de linhas no DataFrame inicial:", df.count())
df = df.filter(col("NIS FAVORECIDO").isNotNull())
print("Total de linhas após remover NIS nulos:", df.count())
df_filtered = df.filter((col("MÊS REFERÊNCIA") >= 201901) & (col("MÊS REFERÊNCIA") <= 201903))
print("Total de linhas após filtro de mês:", df_filtered.count())
total_familias = df_filtered.select(countDistinct("NIS FAVORECIDO").alias("total_familias")).first()["total_familias"]
print(f"Total de famílias beneficiadas (antes de DataFrame): {total_familias}")

df_result = spark.createDataFrame([("Total", total_familias)], ["Descrição", "Valor"])
print("Total de linhas no resultado final:", df_result.count())

df_result.show()
df_result.write.mode("overwrite").parquet("/user/dados/bolsa-familia/resultados/total_familias")

spark.stop()
