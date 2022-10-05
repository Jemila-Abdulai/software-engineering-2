from counterfit_connection import CounterFitConnection
CounterFitConnection.init('127.0.0.1', 5000)

import time
from counterfit_shims_grove.adc import ADC
from counterfit_shims_grove.grove_relay import GroveRelay
import json
from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse

#connection_string = 'HostName=azure-software-engineering-iot-hub.azure-devices.net;DeviceId=soil-moisture-sensor;SharedAccessKey=Tzx2I5OC3U5weQPVM7ZDskkFYxaqK7Z6VG/8JNumVoY='
connection_string = "HostName=StubHub1.azure-devices.net;DeviceId=soil-moisture-sensor;SharedAccessKey=5nmlmsFUQErXJ505PgJyzZuR3ZPRwuTK4dR7j9kvLf8=" # SDR

adc = ADC()
relay = GroveRelay(5)

device_client = IoTHubDeviceClient.create_from_connection_string(connection_string)

print('Connecting')
device_client.connect()
print('Connected')

def handle_method_request(request):
    print("Direct method received - ", request.name)
    
    if request.name == "relay_on":
        relay.on()
    elif request.name == "relay_off":
        relay.off()

    method_response = MethodResponse.create_from_method_request(request, 200)
    device_client.send_method_response(method_response)

device_client.on_method_request_received = handle_method_request

while True:
    try:
      soil_moisture = adc.read(0)
      print("Soil moisture:", soil_moisture)

      message = Message(json.dumps({ 'soil_moisture': soil_moisture }))
      device_client.send_message(message)
      time.sleep(10)
    except Exception as e:
      print("CounterFit.counterfit is not running - please issue \n  python3 Counterfit.counterfit \n... on the command line")
      time.sleep(5)
