import mysql.connector
import datetime

# conexion a la base de datos
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="register",
    port=3308
)

cursor = database.cursor(buffered=True)

class User:

    def __init__(self, vorname, nachname, email, password):  # constructor para registros y logins
        self.vorname = vorname
        self.nachname = nachname
        self.email = email
        self.password = password


    def registrieren(self):

        sql = "INSERT INTO register VALUES(null, %s, %s, %s, %s)"
        dieUser = (self.vorname, self.nachname, self.email, self.password)

        cursor.execute(sql, dieUser)
        database.commit()

        return [cursor.rowcount, self]

    def login(self):
        return self.vorname