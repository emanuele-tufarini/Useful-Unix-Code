'''
pip3 install mysql-connector-python
pip3 install pandas
pip3 install pyspark
'''

import mysql.connector as connection
import pandas as pd

mydb = connection.connect(host="HOSTNAME", 
                          user='USER',
                          password='PASSWORD',
                          database='DATABASE',
                          use_pure=True)

query = "SELECT * FROM TABLE"

pandasDF = pd.read_sql(query,mydb)

#chiudi la connessione

mydb.close()
    
pandasDF.head()

from pyspark.sql import SparkSession

from pyspark import SparkContext

sc = SparkContext.getOrCreate()

#Create PySpark SparkSession

spark = SparkSession.builder.getOrCreate()

#Create PySpark DataFrame from Pandas
sparkDF=spark.createDataFrame(pandasDF) 

sparkDF.printSchema()
