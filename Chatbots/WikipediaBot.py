import wikipedia

# Festlegen der Wikipedia-Sprache (optional)
wikipedia.set_lang("de")  # Hier kann man die Sprache auf "de" für Deutsch setzen, oder auf "en" für Englisch

# Funktion, um die Antwort von Wikipedia zu holen
def get_wikipedia_summary(term):
    try:
        # Holen der Zusammenfassung eines Artikels
        summary = wikipedia.summary(term, sentences=2)  # 2 Sätze als Zusammenfassung
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        # Wenn es mehrere mögliche Bedeutungen gibt
        return f"Es gibt mehrere Bedeutungen für '{term}'. Bitte sei spezifischer. Optionen: {e.options}"
    except wikipedia.exceptions.HTTPTimeoutError:
        # Timeout-Fehler, wenn keine Verbindung zu Wikipedia hergestellt werden kann
        return "Es gab ein Problem beim Abrufen von Informationen von Wikipedia. Bitte versuche es später erneut."
    except wikipedia.exceptions.RedirectError:
        # Fehler, wenn eine Weiterleitung auf eine andere Seite erfolgt
        return "Es wurde auf eine andere Seite umgeleitet. Versuche es mit einem spezifischeren Begriff."
    except wikipedia.exceptions.HTTPError:
        # HTTP-Fehler, wenn der Wikipedia-Server ein Problem hat
        return "Es gab ein Problem beim Abrufen der Seite. Bitte versuche es später erneut."

# Funktion für den Chatbot
def chatbot():
    print("Hallo! Ich bin ein Wikipedia-basierter Chatbot. Wie kann ich dir helfen?")
    
    while True:
        user_input = input("Du: ").lower()
        
        # Folgende Eingaben beenden der Bot das Gespräch
        if user_input in ['tschüss', 'auf wiedersehen', 'ciao','bye','exit']:
            print("Bot: Tschüss! Bis zum nächsten Mal!")
            break
        
        # Abrufen der Antwort von Wikipedia
        print("Bot: Lass mich nachsehen...")
        response = get_wikipedia_summary(user_input)
        
        # Ausgabe der Antwort
        print(f"Bot: {response}")

# Starte den Chatbot
chatbot()
