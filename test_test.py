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

    # If the table doesn't exist, create it
    if not table_exists:
        mycursor.execute(
            "CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID INT AUTO_INCREMENT PRIMARY KEY)"
        )
        print("Table 'Person' created successfully.")

    # Insert new entries or accept new entries into the 'Person' table
    while True:
        name = input("Enter name (or 'quit' to stop): ")
        if name.lower() == "quit":
            break
        age = int(input("Enter age: "))
        mycursor.execute("INSERT INTO Person (name, age) VALUES (%s, %s)", (name, age))
        db.commit()

    # Display the contents of the 'Person' table
    mycursor.execute("SELECT * FROM Person")
    print("Contents of 'Person' table:")
    for x in mycursor:
        print(x)

    # Close the cursor and connection
    mycursor.close()
    db.close()
    print("Connection closed.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
