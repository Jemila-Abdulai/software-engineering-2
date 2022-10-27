
const express = require('express')

let devices = []

const connect = (conn_str, azure_iothub) => azure_iothub.Registry.fromConnectionString(conn_str)

const monitorDevices = (registry, pollTime = 1000) =>
  setInterval(async () => devices = (await registry.list()).responseBody, pollTime)

const devicesToApiDevices = devices => {
  return devices.map(device => {
    return {
      id: device.deviceId,
      alive: device.connectionState === 'Connected'
    }
  })
}
const api_devices = (req, res) => {
  res.json(devicesToApiDevices(devices))
}

const deviceRouter = (sauce, router = express.Router()) => {
  monitorDevices(sauce)
  router.get('/api/devices', api_devices)

  return router
}

module.exports = {
  api_devices,
  deviceRouter,
  devicesToApiDevices,
  connect,
  monitorDevices
}