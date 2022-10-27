const path = require('path')
const fs = require('fs')
const dotenv = require('dotenv')
const express = require('express')
const iothub = require('azure-iothub')

const routes = require('./server/routes.js')

const inProd = !process.env.DEV

let loadedConfig
if (!inProd) {
  const dashboardRoot = path.join(__dirname, '../')
  const envFile = fs.readFileSync(path.join(dashboardRoot, '.env'))
  loadedConfig = dotenv.parse(envFile)
} else {
  loadedConfig = {
    IOT_CONN_STR: process.env.IOT_CONN_STR,
    PORT: process.env.PORT || 8080
  }
}

const requiredEnvVars = [
  'IOT_CONN_STR'
]

const config = {
  IOT_CONN_STR: loadedConfig.IOT_CONN_STR,
  PORT: loadedConfig.PORT || 8080
}

requiredEnvVars.forEach(envVar => {
  if (config[envVar] === undefined) {
    throw Error(`Missing ${envVar} environment variable`)
  }
})

const deviceSauce = inProd
  ? {
    list: async () => {
      return {
        responseBody: {
          devices: [
            { id: 'my-device1', alive: true },
            { id: 'my-device2', alive: false }
          ]
        }
      }
    }
  }
  : routes.connect(config.IOT_CONN_STR, iothub)

// Setup HTTP Server
const app = express()
app.use(express.json())

// Serve webpage resources
app.use('/', express.static(path.join(__dirname, '../', '../', 'dist')))

// Serve device routes
app.use(routes.deviceRouter(deviceSauce))

app.listen(config.PORT, () => {
  console.log(`Example app listening on port ${config.PORT}`)
})