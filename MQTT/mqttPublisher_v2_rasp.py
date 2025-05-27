import paho.mqtt.client as mqtt

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)  # Explizit API Version 2 setzen
client.connect("192.168.13.246", 1883)

client.publish("test/thema", "Hallo MQTT mit API v2 und Raspberry PI als Broker!")
client.disconnect()
print("Nachricht gesendet!")
