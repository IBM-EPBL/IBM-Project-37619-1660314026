import wiotp.sdk.device
import time
import random
myConfig = {
"identity": {
"orgId": "mw7mjd",
"typeId": "NodeMCU",
"deviceId":"12345"
},
"auth": {
"token": "12345678 "
}
}
def myCommandCallback(cmd):
  print("Message received from IBM IoT Platform: %s" %
  cmd.data['command'])
  m=cmd.data['command']
client = wiotp.sdk.device.DeviceClient(config=myConfig,
  logHandlers=None)
client.connect()
while True:
  hgas=0
  gas=random.randint(0,1)
  if(gas==1):
    hgas=random.randint(1,100)
  temp=random.randint(0,100)
  hum=random.randint(0,100)
  pre=random.randint(0,100)
  myData={'Gas':hgas, 'Temperature':temp, 'Humidity':hum, 'Pressure':pre }
  client.publishEvent(eventId="status", msgFormat="json",
  data=myData, qos=0, onPublish=None)
  print("Published data Successfully: %s", myData) 
  client.commandCallback =  myCommandCallback
  time.sleep(5)
client.disconnect()