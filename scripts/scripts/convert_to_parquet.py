from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_replace, col
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
    StructField("VALOR PARCELA", StringType(), True)
])

spark = SparkSession.builder.appName("ConvertToParquet").getOrCreate()

df = spark.read.schema(schema).option("delimiter", ";").option("header", "true").csv("/user/dados/bolsa-familia/csv/*.csv")
df = df.withColumn("VALOR PARCELA", regexp_replace(col("VALOR PARCELA"), ",", ".").cast(DoubleType()))
df.write.mode("overwrite").parquet("/user/dados/bolsa-familia/parquet/")

spark.stop()
