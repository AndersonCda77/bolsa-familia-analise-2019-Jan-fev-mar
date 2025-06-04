from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg as avg_
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

spark = SparkSession.builder.appName("MediaValorFamilia").getOrCreate()

df = spark.read.schema(schema).parquet("/user/dados/bolsa-familia/parquet/*.parquet")
df_grouped = df.groupBy("UF").agg(avg_("VALOR PARCELA").alias("media_valor_familia"))

df_grouped.show()
df_grouped.write.mode("overwrite").parquet("/user/dados/bolsa-familia/resultados/media_valor_familia")

spark.stop()
