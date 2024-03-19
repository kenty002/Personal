import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="kfunada",
    passwd="Kf100219980929!",
    database="testdatabase",
)

users = [("tim", "techwithtim"), ("joe", "joey123"), ("sarah", "sarah1234")]

user_score = [(45, 100), (30, 200), (46, 124)]

# Create a cursor object
mycursor = db.cursor()

Q1 = "CREATE TABLE Users (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), passwd VARCHAR(50))"
Q2 = "CREATE TABLE Scores (userId int PRIMARY KEY, FOREIGN KEY(userId) REFERENCES Users(id), game1 int DEFAULT 0, game2 int DEFAULT 0)"

Q3 = "INSERT INTO Users (name, passwd) VALUES (%s, %s)"
Q4 = "INSERT INTO Scores (userId, game1, game2) VALUES (%s,%s,%s)"

for x, user in enumerate(users):
    mycursor.execute(Q3, user)
    last_id = mycursor.lastrowid
    mycursor.execute(Q4, (last_id,) + user_score[x])

db.commit()

mycursor.execute("SELECT * FROM Scores")
for x in mycursor:
    print(x)

mycursor.execute("Select * FROM Users")
for x in mycursor:
    print(x)
