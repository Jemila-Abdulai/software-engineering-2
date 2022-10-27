const path = require('path')
const fs = require('fs')
const dotenv = require('dotenv')
const express = require('express')
const iothub = require('azure-iothub')

const routes = require('./server/routes.js')

const inDev = process.env.DEV

let config = {}
if (inDev) {
  const dashboardRoot = path.join(__dirname, '../')
  const envFile = fs.readFileSync(path.join(dashboardRoot, '.env'))
  config = dotenv.parse(envFile)
} else {
  config.IOT_CONN_STR =   `${process.env.IOT_HOST_NAME};${process.env.IOT_SHARED_ACCESS_KEY_NAME};${process.env.IOT_SHARED_ACCESS_KEY}`
  config.PORT = process.env.PORT || 8080
}

const requiredEnvVars = [
  'IOT_CONN_STR'
]

requiredEnvVars.forEach(envVar => {
  if (config[envVar] === undefined) {
    throw Error(`Missing ${envVar} environment variable`)
  }
})

const deviceSauce = inDev
  ? {
    list: async () => {
      return  [
        {
          deviceId: "soil-moisture-sensor",
          generationId: "637993504504538781",
          etag: "ODgxNjE4MDQx",
          connectionState: "Disconnected",
          status: "enabled",
          statusReason: null,
          connectionStateUpdatedTime: "2022-10-20T07:45:31.9363936Z",
          statusUpdatedTime: "0001-01-01T00:00:00Z",
          lastActivityTime: "2022-10-13T13:58:41.8528977Z",
          cloudToDeviceMessageCount: 0,
          capabilities: {
          },
          authentication: {
            symmetricKey: {
              primaryKey: "Tzx2I5OC3U5weQPVM7ZDskkFYxaqK7Z6VG/8JNumVoY=",
              secondaryKey: "a++0/406emVj+DVFUBHrrmWcYHjQ/PnzbPiHT5twmJI=",
            },
            x509Thumbprint: {
              primaryThumbprint: null,
              secondaryThumbprint: null,
            },
            type: "sas",
            SymmetricKey: {
              primaryKey: "Tzx2I5OC3U5weQPVM7ZDskkFYxaqK7Z6VG/8JNumVoY=",
              secondaryKey: "a++0/406emVj+DVFUBHrrmWcYHjQ/PnzbPiHT5twmJI=",
            },
          },
        },
      ]
    }
  }
  : routes.connect(config.IOT_CONN_STR, iothub)

// Setup HTTP Server
const app = express()
app.use(express.json())

// Serve webpage resources
app.use('/', express.static(path.join(__dirname, '../', 'dist')))

// Serve device routes
app.use(routes.deviceRouter(deviceSauce))

app.listen(config.PORT, () => {
  console.log(`Dashboard listening on port ${config.PORT}`)
})