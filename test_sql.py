import mysql.connector

try:
    # Connect to MySQL
    db = mysql.connector.connect(
        host="localhost",
        user="kfunada",
        passwd="Kf100219980929!",
        database="testdatabase",
    )

    # Create a cursor object
    mycursor = db.cursor()

    # Check if the 'Person' table exists
    mycursor.execute("SHOW TABLES LIKE 'Person'")
    table_exists = mycursor.fetchone()

    # If the table exists, drop it
    if table_exists:
        mycursor.execute("DROP TABLE Person")
        print("Table 'Person' dropped successfully.")
    else:
        print("Table 'Person' does not exist.")

    # Create the 'Person' table again
    mycursor.execute(
        "CREATE TABLE IF NOT EXISTS Person (name VARCHAR(50), age smallint UNSIGNED, personID INT PRIMARY KEY AUTO_INCREMENT)"
    )

    # Insert some sample data into the 'Person' table
    mycursor.execute("INSERT INTO Person (name, age) VALUES (%s, %s)", ("Joe", 12))
    db.commit()

    # Display the contents of the 'Person' table
    mycursor.execute("SELECT * FROM Person")
    for x in mycursor:
        print(x)

    # Close the cursor and connection
    mycursor.close()
    db.close()
    print("Table 'Person' reset successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
