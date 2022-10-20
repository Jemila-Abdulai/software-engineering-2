// Load environment variables from .env file
require('dotenv').config()

const path = require('path')
const express = require('express')
const iothub = require('azure-iothub')

const inProd = !process.env.DEV

const requiredEnvVars = [
  'IOT_CONN_STR'
]

const config = {
  IOT_CONN_STR: process.env.IOTHUB_CONN_STR,
  PORT: process.env.PORT || 8080
}

requiredEnvVars.forEach(envVar => {
  if (config[envVar] === undefined) {
    throw Error(`Missing ${envVar} environment variable`)
  }
})

let devices = [
  { id: 'my-device1', alive: true },
  { id: 'my-device2', alive: false }
]

if (!inProd) {
  devices = [
    { id: 'my-device1', alive: true },
    { id: 'my-device2', alive: false }
  ]
} else {
  const iothubRegistry = iothub.Registry.fromConnectionString(config.IOT_CONN_STR)
  setInterval(async () => {
    const res = await iothubRegistry.list()
    devices = res.responseBody
  }, 1000)
}

// Setup HTTP Server
const app = express()
app.use(express.json())

const root = path.join(__dirname, '../', '../')
app.use('/', express.static(path.join(root, 'dist')))

app.get('/api/devices', (req, res) => {
  const deviceList = devices.map(device => {
    return {
      id: device.deviceId,
      alive: device.connectionState === 'Connected'
    }
  })
  res.json(deviceList)
})

app.listen(config.PORT, () => {
  console.log(`Example app listening on port ${config.PORT}`)
})