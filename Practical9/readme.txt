Install

1. sudo wget http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key
2. sudo apt-key add mosquitto-repo.gpg.key
3. cd /etc/apt/sources.list.d/
4. sudo wget http://repo.mosquitto.org/debian/mosquitto-stretch.list
5. sudo apt-get update
6. sudo apt-get install mosquitto mosquitto-clients
7. sudo pip3 install paho-mqtt

Configure 
1. cd /etc/mosquitto
2. sudo cp mosquitto.conf mosquitto.conf.original
3. sudo nano mosquito.conf

Subscribe
mosquitto_sub -d -t 'test/mosquitto'

Publish (same machine, different terminal)
mosquitto_pub -d -t 'test/mosquitto' -m 'This is test message'

________

Python code:
mqttPublish.py

import paho.mqtt.client as mqtt
broker_address = "192.168.0.202"
client = mqtt.Client("P1")
client.connect(broker_address)
client.publish("test/mosquitto", "This is from MQTT Python")


(Use IP or locahost)

sudo python3 mqttPublish.py