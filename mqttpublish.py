import paho.mqtt.client as paho
import time
client = paho.Client()
client.connect("broker.mqttdashboard.com", 1883) # Public broker
client.loop_start()

while True:
	client.publish("testtopic/1", "asd") #Publishing path
	print("Sent")
	time.sleep(5)