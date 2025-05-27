import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print(f"Nachricht empfangen: {message.payload.decode()} auf Thema {message.topic}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)  # Explizit API Version 2 setzen
client.on_message = on_message

client.connect("localhost", 1883)
client.subscribe("test/thema")

print("Warte auf Nachrichten...")
client.loop_forever()
