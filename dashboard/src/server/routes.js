
const express = require('express')

let deviceList = []

const devicesToApiDevices = devices => {
  return devices.map(device => {
    return {
      id: device.deviceId,
      alive: device.connectionState === 'Connected'
    }
  })
}
const api_devices = (req, res) => {
  res.json(devicesToApiDevices(deviceList))
}

const deviceRouter = (devices, router = express.Router()) => {
  deviceList = devices
  router.get('/api/devices', api_devices)

  return router
}

module.exports = {
  api_devices,
  deviceRouter,
  devicesToApiDevices,
  deviceList
}