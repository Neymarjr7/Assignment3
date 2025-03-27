import paho.mqtt.client as mqtt
import random
import time

def generate_sensor_data():
    temperature = round(random.uniform(-50, 50), 2)
    humidity = round(random.uniform(0, 100), 2)
    co2 = random.randint(300, 2000)
    return temperature, humidity, co2

MQTT_BROKER = "mqtt3.thingspeak.com"
MQTT_PORT = 1883
MQTT_USERNAME = "2894293"
MQTT_PASSWORD = "E1AYH6E1LO0G9JUJ"
MQTT_TOPIC = "channels/2894293/publish/E1AYH6E1LO0G9JUJ"

client = mqtt.Client()
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to ThingSpeak MQTT!")
    else:
        print(f"Failed to connect, return code {rc}")

def on_publish(client, userdata, mid):
    print("Data Published to ThingSpeak")

client.on_connect = on_connect
client.on_publish = on_publish

client.connect(MQTT_BROKER, MQTT_PORT, 120)

def send_sensor_data():
    while True:
        temp, hum, co2 = generate_sensor_data()
        payload = f"field1={temp}&field2={hum}&field3={co2}"
        client.publish(MQTT_TOPIC, payload)
        print(f"Published: {payload}")
        time.sleep(15)

send_sensor_data()
