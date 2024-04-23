# import the connect method
import os

from mysql.connector import connect
from dotenv import load_dotenv

load_dotenv()

passw = os.getenv("DB_PASS")

# define a connection object
conn = connect(
    user='sergio',
    password='Sergio123@',
    host='100.97.64.6',
    database='Club')

cursor = conn.cursor()
query = 'SELECT * FROM Jugador'
cursor.execute(query)
result = cursor.fetchall()

# print the results in each row
for r in result:
    print(r)

# close the cursor and database connection
cursor.close()
conn.close()

print('A connection object has been created.')

# close the database connection
conn.close()