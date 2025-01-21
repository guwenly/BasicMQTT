import paho.mqtt.client as paho
import RPi.GPIO as GPIO
import time

def kapiac():
    pin = 21

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(1)

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    if "kapi" in str(msg.payload):
        try:
            kapiac()
            print("Kapı açıldı.")
        except KeyboardInterrupt as e:
            print(e)
        finally:
            GPIO.cleanup()

client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect("broker.mqttdashboard.com", 1883) # Public broker
client.subscribe("testtopic/1") #Listening path

client.loop_forever()