import sys
import pandas as pd
import csv
from datetime import datetime
from data_entry import *
import paho.mqtt.client as paho
import random
import json
import threading
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
class CSV:
    csv_fille = "finance_data.csv"
    Columns = ["date","amount","category","description"]
    @classmethod
    def initializeCSV(cls):
        try:
            pd.read_csv(cls.csv_fille)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.Columns)
            df.to_csv(cls.csv_fille, index=False)
    @classmethod
    def add_csv_entry(cls,date,amount,category,description):
        new_entry={"date":date,"amount":amount,"category":category,"description":description}
        with open(cls.csv_fille, "a",newline="") as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=cls.Columns)
            writer.writerow(new_entry)
            client.publish("test/status",json.dumps(new_entry),0)
        print("Entry added Successfully /n",new_entry)

def add():
    CSV.initializeCSV()
    CSV.add_csv_entry(get_date("Enter the date of transaction (dd-mm-yyyy) or press 'enter' for today's date:",allow_default=True),get_amount(),get_category(),get_description())

def listen():
    try:
        print("start")
        client.loop_forever()
    except:
        print("disconnect")
threading.Thread(target=add).start()
threading.Thread(target=listen).start()
