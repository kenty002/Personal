import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="kfunada",
    password="Kf100219980929!",
    database="my_database",
)

# Create a new table
cursor = connection.cursor()
cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS my_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            age INT
        )
    """
)
print("Table 'my_table' created successfully!")


# Get table structure
cursor.execute("DESCRIBE my_table")
rows = cursor.fetchall()

# Display the table structure
print("Structure of 'my_table':")
for row in rows:
    print(row)

# Close cursor and connection
cursor.close()
connection.close()
print("Connection closed.")
