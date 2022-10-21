const iothub = require('azure-iothub')

const connect = (conn_str, azure_iothub) => azure_iothub.Registry.fromConnectionString(config.IOT_CONN_STR)

const monitorDevices = (registry, pollTime = 1000) => {
  let devices
  const interval = setInterval(async () => devices = (await iothubRegistry.list()).responseBody, pollTime)
  return {
    devices,
    interval
  }
}

module.exports = {
  connect,
  monitorDevices
}