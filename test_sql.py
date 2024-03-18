import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="kfunada",
    passwd="Kf100219980929!",
    database="testdatabase",
)

# Create a cursor object
mycursor = db.cursor()

# Create the 'Person' table
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Person (name VARCHAR(50), age smallint UNSIGNED, personID INT PRIMARY KEY AUTO_INCREMENT)"
)

# Describe the table
mycursor.execute("DESCRIBE Person")
print("Table structure:")
for column in mycursor:
    print(column)

# Close the cursor and connection
mycursor.close()
db.close()
