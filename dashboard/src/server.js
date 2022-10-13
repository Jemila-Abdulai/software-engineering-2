const path = require('path')
const express = require('express')
const app = express()
const port = 8081

const root = path.join(__dirname, '../', '../')
const mock_data = [
  { id: 5673, device_name: 'soil_sensor_1', alive: true },
  { id: 5612, device_name: 'soil_sensor_2', alive: true },
  { id: 5243, device_name: 'soil_sensor_3', alive: false }
]

app.use(express.json())

// Serve the build
app.use('/', express.static(path.join(root, 'dist')))

app.get('/api/devices', (req, res) => {
  res.json(mock_data)
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})