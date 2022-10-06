const path = require('path')
const express = require('express')
const app = express()
const port = 8081

const root = path.join(__dirname, '../', '../')

app.use(express.json())

// Serve the build
app.use('/', express.static(path.join(root, 'dist')))

app.get('/api/hello', (req, res) => {
  res.json('Hello World!')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})