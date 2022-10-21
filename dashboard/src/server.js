// Load environment variables from .env file
require('dotenv').config()

const path = require('path')
const express = require('express')

const routes = require('./server/routes.js')
const azure = require('./server/azure.js')

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
let iothubRegistry

if (inProd) {
  devices = []
  iothubRegistry = azure.connect(config.IOT_CONN_STR)
  devices = azure.monitorDevices(iothubRegistry).devices
}

// Setup HTTP Server
const app = express()
app.use(express.json())

// Serve webpage resources
app.use('/', express.static(path.join(__dirname, '../', '../', 'dist')))

// Serve device routes
app.use(routes.deviceRouter())

app.listen(config.PORT, () => {
  console.log(`Example app listening on port ${config.PORT}`)
})