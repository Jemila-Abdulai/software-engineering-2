
const express = require('express')

let deviceList

const api_devices = (req, res) => {
  res.json(deviceList.map(device => {
    return {
      id: device.deviceId,
      alive: device.connectionState === 'Connected'
    }
  }))
}

const deviceRouter = (devices, router = express.Router()) => {
  deviceList = devices
  router.get('/api/devices', api_devices)

  return router
}

module.exports = {
  api_devices,
  deviceRouter
}