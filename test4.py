import mysql.connector
from datetime import datetime

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="kfunada",
    passwd="Kf100219980929!",
    database="testdatabase",
)

# Create a cursor object
mycursor = db.cursor()
# mycursor.execute(
#     "CREATE TABLE Test (name varchar(50) NOT NULL, created datetime NOT NULL, gender ENUM('M', 'F', 'O') NOT NULL , id int PRIMARY KEY NOT NULL AUTO_INCREMENT)"
# )

# mycursor.execute(
#     "INSERT INTO Test (name,created,gender) VALUES (%s,%s,%s)",
#     ("JOE", datetime.now(), "M"),
# )

# mycursor.execute("SELECT * FROM Test WHERE gender = 'M' ORDER BY id DESC")

# mycursor.execute("ALTER TABLE Test ADD COLUMN food VARCHAR(50) NOT NULL")

mycursor.execute("ALTER TABLE Test CHANGE name first_name VARCHAR(50)")

mycursor.execute("DESCRIBE Test")

for x in mycursor:
    print(x)
