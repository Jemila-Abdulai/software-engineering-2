const connect = (conn_str, azure_iothub) => azure_iothub.Registry.fromConnectionString(conn_str)

const monitorDevices = (registry, pollTime = 1000) => {
  let devices
  return {
    devices,
    interval: setInterval(async () => devices = await registry.list().responseBody, pollTime)
  }
}

module.exports = {
  connect,
  monitorDevices
}