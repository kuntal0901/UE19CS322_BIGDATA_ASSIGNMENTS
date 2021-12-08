import sys
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import avg,count,max
from pyspark.sql import Row
sql_context = SQLContext(SparkContext.getOrCreate())
citypath,globalpath=sys.argv[1:]
df_city = sql_context.read.csv(citypath, header=True)
df_global=sql_context.read.csv(globalpath, header=True)

df_global=df_global.withColumn("LandAverageTemperature",df_global["LandAverageTemperature"].cast("double"))
df_city=df_city.withColumn("AverageTemperature",df_city["AverageTemperature"].cast("double"))

max_city =df_city.groupBy("dt","Country").agg(max("AverageTemperature").alias("max")).orderBy('dt')
df=df_global.join(max_city,df_global.dt==max_city.dt,"inner").drop(max_city.dt)
df=df.filter(df.max>df_global.LandAverageTemperature).groupBy('Country').agg(count('Country')).orderBy(df.Country).collect()
for i in df:
    print("{}\t{}".format(i["Country"],i["count(Country)"]))
