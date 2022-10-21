
const express = require('express')

const api_devices = (req, res) => {
  const deviceList = devices.map(device => {
    return {
      id: device.deviceId,
      alive: device.connectionState === 'Connected'
    }
  })
  res.json(deviceList)
}

const deviceRouter = () => {
  const router = express.Router()

  router.get('/api/devices', api_devices)

  return router
}

module.exports = {
  api_devices,
  deviceRouter
}