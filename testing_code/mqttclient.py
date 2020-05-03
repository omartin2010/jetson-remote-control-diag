import paho.mqtt.client as mqtt
# import time
import json
from numpy import pi
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(threadName)s:%(message)s')
log = logging.getLogger(__name__)

client = mqtt.Client()
client.enable_logger(logger=log)
client.connect("192.168.32.56", 1883)
i = 0

jsonpayload = {
    "x": 1,
    "y": 0,
    "phi": pi / 2,
    "control_method": 'velocity',
    "velocity_factor": 0.1,
    "dryrun": True
}
payload = json.dumps(jsonpayload)

while True:
    i += 1
    msg = client.publish(topic="bot/base/move/xyphi", payload=payload, qos=0)
    print("done loop {}... msg published = {}".format(i, msg.is_published()))
    # time.sleep(20)
