import paho.mqtt.client as paho
import random
import json
import sys
client_id = f'python-mqtt-{random.randint(0, 1000)}'
calback = paho.CallbackAPIVersion.VERSION1
client = paho.Client(calback, client_id)
def message(client,userdata,msg):
    print(msg.topic+": "+msg.payload.decode())

client.on_message=message
if client.connect("broker.emqx.io",1883, 60) != 0:
    print("Could not connect to the MQTT broker!!!")
    sys.exit(-1)
else:
    print("connencted to client")


client.subscribe("test/status")

try:
    print("start")
    client.loop_forever()
except:
    print("disconnect")

client.disconnect()
