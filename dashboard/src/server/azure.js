const connect = (conn_str, azure_iothub) => azure_iothub.Registry.fromConnectionString(conn_str)

const monitorDevices = (registry, pollTime = 1000) => {
  let devices
  const interval = setInterval(async () => devices = await registry.list().responseBody, pollTime)
  return {
    devices,
    interval
  }
}

module.exports = {
  connect,
  monitorDevices
}