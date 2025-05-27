import sqlite3
from pathlib import Path

skript_verzeichnis = Path(__file__).resolve().parent
db = skript_verzeichnis / "daten" / "meine_datenbank.db"



# Verbindung aufbauen
conn = sqlite3.connect(db)
cursor = conn.cursor()

# Tabelle erstellen
cursor.execute("""
CREATE TABLE IF NOT EXISTS benutzer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    alter_jahre INTEGER
)
""")

# Daten einfügen
cursor.execute("INSERT INTO benutzer (name, alter_jahre) VALUES (?, ?)", ("Felix", 25))
cursor.execute("INSERT INTO benutzer (name, alter_jahre) VALUES (?, ?)", ("Florian", 25))
cursor.execute("INSERT INTO benutzer (name, alter_jahre) VALUES (?, ?)", ("Strolch", 5))

conn.commit()

# Daten abfragen
cursor.execute("SELECT * FROM benutzer")
for zeile in cursor.fetchall():
    print(zeile)

# Verbindung schließen
conn.close()
