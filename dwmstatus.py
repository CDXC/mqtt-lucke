import time
import json
import os
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
t = ''
a = open('/usr/local/sbin/auth', 'r')
content = a.read()
u,p,x = content.split("\n")

def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

c = mqtt.Client()
c.username_pw_set(username=u,password=p)
c.on_connect=on_connect

def on_message(client, userdata, message):
	global t
	pack = json.loads(message.payload)
	t = str(pack["BME280"]["Temperature"]) + str(pack["TempUnit"] + "C° ")
	
c.connect("192.168.1.10", port=1883, keepalive=60,bind_address="")
c.loop_start()
c.on_message=on_message
c.subscribe("tele/pm10n2/SENSOR")
while True:
	status = 'xsetroot -name "$(date)"  ' + t
	os.system(status)
	time.sleep(1) 

c.loop.stop()
	
