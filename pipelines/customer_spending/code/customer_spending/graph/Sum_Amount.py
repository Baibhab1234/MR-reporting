from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customer_spending.config.ConfigStore import *
from customer_spending.udfs.UDFs import *

def Sum_Amount(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("c_custkey"), month(col("o_orderdate")).alias("Month"))

    return df1.agg(sum(col("o_totalprice")).alias("Amount"))
