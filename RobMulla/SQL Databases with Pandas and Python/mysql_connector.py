import mysql.connector

connection = mysql.connector.connect(
    user='ami_ro_ryan',
    password='Rjhf5v^a9Wke',
    host='192.168.102.159',
    database='wBSC',
)
print(connection)
cursor = connection.cursor()

query = """select * from devices"""
cursor.execute(query)
for i, data in enumerate(cursor):
    break
print(data)

connection.close()
cursor.close()