from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customer_spending.config.ConfigStore import *
from customer_spending.udfs.UDFs import *

def Join_by_CustId(spark: SparkSession, in0: DataFrame, in1: DataFrame, ) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.c_custkey") == col("in1.o_custkey")), "inner")\
        .select(col("in0.c_custkey").alias("c_custkey"), col("in1.o_totalprice").alias("o_totalprice"), col("in1.o_orderdate").alias("o_orderdate"))
