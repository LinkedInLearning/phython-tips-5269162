import openai
import os

# Setze den API-Schlüssel
openai.api_key = ""  # Oder über Umgebungsvariable: os.getenv("OPENAI_API_KEY")

def chat_with_gpt(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # oder gpt-4, wenn verfügbar
            messages=[
                {"role": "system", "content": "Du bist ein hilfreicher, freundlicher Assistent."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=200
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Fehler bei der API-Anfrage: {e}"

def chatbot():
    print("GPT-Chatbot gestartet! Tippe 'exit', um zu beenden.")
    while True:
        user_input = input("Du: ")
        if user_input.lower() == "exit":
            print("Bot: Auf Wiedersehen!")
            break
        reply = chat_with_gpt(user_input)
        print(f"Bot: {reply}")

chatbot()
