import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="kfunada",
    passwd="Kf100219980929!",
    database="testdatabase",
)
mycursor = db.cursor()


# Check if the table exists
mycursor.execute("SHOW TABLES LIKE 'Person'")
table_exists = mycursor.fetchone()

# If the table doesn't exist, create it
if not table_exists:
    mycursor.execute(
        "CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID INT PRIMARY KEY AUTO_INCREMENT)"
    )
    print("Table 'Person' created successfully.")
else:
    print("Table 'Person' already exists.")

# Describe the table
mycursor.execute("DESCRIBE Person")
print("Table structure:")
for column in mycursor:
    print(column)

# Close the cursor and connection
mycursor.close()
db.close()
