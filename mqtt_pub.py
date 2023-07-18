import paho.mqtt.client as mqtt
import time

broker_address = "localhost"  
broker_port = 1883  

def on_connect(client, userdata, flags, rc):
   print("Connected") 

client = mqtt.Client()

client.on_connect = on_connect

client.connect(broker_address, broker_port, 60)

client.loop_start()
time.sleep(1)

client.publish("topic/1", "Hello Iam Host")

client.loop_stop()
client.disconnect()



