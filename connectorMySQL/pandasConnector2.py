'''
pip3 install pymysql
pip3 install pandas
'''

import pymysql.cursors

connection = pymysql.connect(host='HOSTNAME',
                             user='USER',
                             password='PASSWORD',
                             database='DATABASE',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

mycursor = connection.cursor()

mycursor.execute("SELECT * FROM TABLE")

myresult = mycursor.fetchall()

for x in myresult: print(x)
