const routes = require('../../src/server/routes.js')

const mockExpressApp = () => {
  return {
    get: jest.fn()
  }
}

describe('routes.js', () => {
  describe('deviceRouter', () => {
    it('creates a device router', () => {
      const app = mockExpressApp()
      routes.deviceRouter({}, app)
      expect(app.get).toHaveBeenCalledWith('/api/devices', routes.api_devices)
    })

    it('creates a device router with the default express router', () => {
      routes.deviceRouter({}) // coverage moans at me
    })
  })

  describe('api_devices', () => {
    routes.deviceList = []
    const res = { json: jest.fn() }
    const req = {}
    routes.api_devices(req, res)
    expect(res.json).toHaveBeenCalledWith(routes.deviceList)
  })

  describe('devicesToApiDevices', () => {
    it('converts device list from azure to the device API format', () => {
      const devices = [
        { deviceId: '1', connectionState: 'Connected' },
        { deviceId: '0', connectionState: 'Disconnected' }
      ]
      expect(routes.devicesToApiDevices(devices)).toEqual([
        { id: '1', alive: true },
        { id: '0', alive: false }
      ])
    })
  })
})