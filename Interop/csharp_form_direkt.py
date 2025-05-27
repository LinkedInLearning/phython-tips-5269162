import clr

# .NET-Namespaces importieren
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form, Button, Label
from System.Drawing import Point

# Form erstellen
form = Form()
form.Text = "WinForms in Python"
form.Width = 300
form.Height = 200

# Label erstellen
label = Label()
label.Text = "Starttext"
label.Location = Point(30, 30)
label.Width = 200

# Button erstellen
button = Button()
button.Text = "Klick mich!"
button.Location = Point(30, 70)

# Klick-Event binden
def on_click(sender, args):
    label.Text = "Button wurde geklickt!"

button.Click += on_click

# Controls zur Form hinzufügen
form.Controls.Add(label)
form.Controls.Add(button)

# GUI starten
Application.Run(form)
