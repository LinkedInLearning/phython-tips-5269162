import clr
import sys
import os

# Pfad zur kompilierten DLL hinzufügen
clr.AddReference(os.path.abspath("WinFormInterop.dll"))

from WinFormInterop import MainForm

form = MainForm()
form.ShowForm()
