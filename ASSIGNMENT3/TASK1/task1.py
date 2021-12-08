import sys
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import avg,count
sql_context = SQLContext(SparkContext.getOrCreate())
country,path=sys.argv[1:]
df = sql_context.read.csv(path, header=True)
df = df.filter(df.Country==country)
avg_city = df.groupBy("City").agg(avg("AverageTemperature").alias("avv"))
df=df.join(avg_city,df.City==avg_city.City,"inner").drop(avg_city.City)
df=df.filter(df.AverageTemperature > df.avv).groupBy('City').agg(count('City')).orderBy(df.City).collect()
for i in df:
    print(f'{i["City"]}\t{i["count(City)"]}')
