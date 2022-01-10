'''
pip3 install mysql-connector-python
pip3 install pandas
pip3 install pyspark
'''

import mysql.connector
import pandas as pd
from pyspark.sql import SparkSession

appName = "pyspark mysql connector"
master = "local"

spark = SparkSession.builder.master(master).appName(appName).getOrCreate()

#stabilire una connessione con il database mysql

connection = mysql.connector.connect(user='USER', database='DATABASE',
                               password='PASSWORD',
                               host="HOSTNAME",
                               port=3306)
cursor = conn.cursor()

query = "SELECT * FROM TABLE"

#creare un dataframe pandas

pdf = pd.read_sql(query, connection)

conn.close()

#convertire il dataframe pandas in dataframe spark

df = spark.createDataFrame(pdf)

#esportare il dataframe spark in formato csv

df.toPandas().to_csv('results.csv')
