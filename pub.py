import paho.mqtt.client as mqtt
 
def on_connect(client, userdata, flags, rc):
client.subscribe("test")
client.publish("test","python hello")
 
def on_message(client, userdata, msg):
print(msg.topic+" "+str(msg.payload))
 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect("blog.cleverize.life", 1883, 60)
