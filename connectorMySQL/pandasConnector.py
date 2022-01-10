'''
pip3 install mysql-connector-python
pip3 install pandas
'''

import mysql.connector as connection
import pandas as pd

mydb = connection.connect(host="HOSTNAME", 
                          user='USER',
                          password='PASSWORD',
                          database='DATABASE',
                          use_pure=True)

query = 'SELECT * FROM TABLE'

pandasDF = pd.read_sql(query,mydb)

mydb.close()
