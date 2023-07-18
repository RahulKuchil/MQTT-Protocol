import paho.mqtt.client as mqtt

broker_address ="localhost" 
#"broker.hivemq.com"  
broker_port = 1883 

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code: " + str(rc))
    client.subscribe("topic/1")

def on_message(client, userdata, msg):
    print("Received messages: " + str(msg.payload.decode()))

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, broker_port, 60)

client.loop_start()

while True:
    pass
