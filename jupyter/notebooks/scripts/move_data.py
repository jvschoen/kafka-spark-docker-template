##Read 
df_visitors = spark.read.parquet('s3://think-training-data-us-east-1-prod-teal/advanceautoparts/main/all-visitors/')
##Filter
df_visitors = df_visitors.where("visit_day >= '2020-08-01'") 

#Write
(
    df_visitors
    .repartition("visit_day")
    .write
    .option('compression', 'snappy')
    .mode("overwrite")
    .partitionBy("visit_day")
    .parquet("s3://jvs-fraud-research/advance_auto_glue_out_by_day")
)