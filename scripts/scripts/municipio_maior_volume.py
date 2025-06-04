from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as sum_
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

spark = SparkSession.builder.appName("MunicipioMaiorVolume").getOrCreate()

df = spark.read.schema(schema).parquet("/user/dados/bolsa-familia/parquet/*.parquet")
df_filtered = df.filter(col("MÊS REFERÊNCIA") == 201902)
df_grouped = df_filtered.groupBy("NOME MUNICÍPIO").agg(sum_("VALOR PARCELA").alias("total_valor"))
df_result = df_grouped.orderBy(col("total_valor").desc()).limit(1)

df_result.show()
df_result.write.mode("overwrite").parquet("/user/dados/bolsa-familia/resultados/municipio_maior_volume")

spark.stop()
