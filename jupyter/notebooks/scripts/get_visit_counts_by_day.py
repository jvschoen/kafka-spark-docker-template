
from pyspark.context import SparkContext
from awsglue.context import GlueContext

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

df_visits = spark.read.parquet("s3://jvs-fraud-research/advance_auto_glue_out_by_day")
df_visits.createOrReplaceTempView("visits")

df_visit_counts_by_day = spark.sql(('''
SELECT 
    visit_day,
    COUNT(visitor_id) num_visits
FROM visits
GROUP BY 
    visit_day
'''))
(
    df_visit_counts_by_day
    .coalesce(1)
    .write
    .format('csv')
    .option('header', True)
    .mode('overwrite')
    .option('sep',',')
    .save('s3://jvs-fraud-research/datasets/visit_counts_by_day')
)
