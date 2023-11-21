from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from customer_spending.config.ConfigStore import *
from customer_spending.udfs.UDFs import *
from prophecy.utils import *
from customer_spending.graph import *

def pipeline(spark: SparkSession) -> None:
    df_order_source = order_source(spark)
    df_customer_Source = customer_Source(spark)
    df_Join_by_CustId = Join_by_CustId(spark, df_customer_Source, df_order_source)
    df_Sum_Amount = Sum_Amount(spark, df_Join_by_CustId)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/customer_spending")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/customer_spending", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/customer_spending")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
