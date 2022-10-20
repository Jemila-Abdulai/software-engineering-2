from counterfit_connection import CounterFitConnection
import time
from counterfit_shims_grove.adc import ADC
from counterfit_shims_grove.grove_relay import GroveRelay
import json
from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse

# azure-software-engineering-iot-hub used - part of our assignment group's resource group
connection_string = 'HostName=azure-software-engineering-iot-hub.azure-devices.net;DeviceId=soil-moisture-sensor;SharedAccessKey=Tzx2I5OC3U5weQPVM7ZDskkFYxaqK7Z6VG/8JNumVoY='
device_client = IoTHubDeviceClient.create_from_connection_string(connection_string)
adc = ADC()
relay = GroveRelay(5)

def establish_connection():
  while True:
    try:
      # Establish a connection on port 5000 on localhost
      CounterFitConnection.init('127.0.0.1', 5000)
      break
    except Exception as e:
      # Exception handling should connection fail to establish
      print("CounterFit.counterfit is likely not running - please issue \n  python3 Counterfit.counterfit \n... on the command line")

      # Retry connection to CounterFit every 5 seconds until successful
      time.sleep(5)


def handle_method_request(request):
  print("Direct method received - ", request.name)
  
  # It is unknown exactly what this if/else condition does - was here already and is not used
  if request.name == "relay_on":
    relay.on()
  elif request.name == "relay_off":
    relay.off()

  method_response = MethodResponse.create_from_method_request(request, 200)
  device_client.send_method_response(method_response)


def main():
  # Try to establish connection with CounterFit
  establish_connection()
  device_client.on_method_request_received = handle_method_request
  while True:
    try:
      # Read pin 0 for soil moisture
      soil_moisture = adc.read(0)
      print("Soil moisture:", soil_moisture)

      # Send JSON payload to CounterFit, detailing soil moisture value received from pin
      message = Message(json.dumps({ 'soil_moisture': soil_moisture }))
      device_client.send_message(message)

      # Read pin for soil moisture every 10 seconds
      time.sleep(10)
    except Exception as e:
      # Exception handling should pin be unreadable
      print("Please ensure a soil moisture sensor is configured on pin 0... http://localhost:5000")

      # Retry reading pin after 5 seconds
      time.sleep(5)

if __name__ == '__main__':
  main()