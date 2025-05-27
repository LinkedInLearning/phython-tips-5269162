import mysql.connector

# Verbindung zur MariaDB/MySQL-Datenbank herstellen
conn = mysql.connector.connect(
    host="localhost",
    user="root",         # ⇐ Benutzername
    password="",     # ⇐ Passwort
    database="test"
)

cursor = conn.cursor()

# Tabelle erstellen (falls nicht vorhanden)
cursor.execute("""
CREATE TABLE IF NOT EXISTS benutzer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    alter_jahre INT
)
""")

# Benutzer einfügen und ID ausgeben
def benutzer_einfuegen(name, alter):
    sql = "INSERT INTO benutzer (name, alter_jahre) VALUES (%s, %s)"
    cursor.execute(sql, (name, alter))
    conn.commit()
    neue_id = cursor.lastrowid
    print(f"Benutzer '{name}' wurde eingefügt mit ID: {neue_id}")

benutzer_einfuegen("Strolch", 5)
benutzer_einfuegen("Susi", 5)

# Alle Benutzer anzeigen
cursor.execute("SELECT * FROM benutzer")
print("\nAlle Benutzer:")
for zeile in cursor.fetchall():
    print(zeile)

# Verbindung schließen
cursor.close()
conn.close()
