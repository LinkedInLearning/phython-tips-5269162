import smtplib
from email.mime.text import MIMEText

# Zugangsdaten
mail_adresse = ""
passwort = ""

# Empfängeradresse
empfaenger = ""

# Nachricht
nachricht = MIMEText("Hallo, das ist eine E-Mail, gesendet von Python über GMX.")
nachricht["Subject"] = "Testmail von Python"
nachricht["From"] = mail_adresse
nachricht["To"] = empfaenger

# E-Mail senden
with smtplib.SMTP_SSL("mail.gmx.net", 465) as server:
    server.login(mail_adresse, passwort)
    server.send_message(nachricht)

print("E-Mail erfolgreich gesendet.")
