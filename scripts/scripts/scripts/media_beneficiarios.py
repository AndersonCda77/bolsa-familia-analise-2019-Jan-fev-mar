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

spark = SparkSession.builder.appName("MediaBeneficiarios").getOrCreate()

df = spark.read.schema(schema).parquet("/user/dados/bolsa-familia/parquet/*.parquet")
print("Total de linhas no DataFrame inicial:", df.count())
df = df.filter(col("NIS FAVORECIDO").isNotNull())
print("Total de linhas após remover NIS nulos:", df.count())
df_grouped = df.groupBy("UF", "NOME MUNICÍPIO").agg(countDistinct("NIS FAVORECIDO").alias("beneficiarios"))
print("Total de linhas após agrupamento por UF e município:", df_grouped.count())
df_result = df_grouped.groupBy("UF").agg({"beneficiarios": "avg"}).withColumnRenamed("avg(beneficiarios)", "media_beneficiarios")
print("Total de linhas no resultado final:", df_result.count())

df_result.show()
df_result.write.mode("overwrite").parquet("/user/dados/bolsa-familia/resultados/media_beneficiarios")

spark.stop()
