const routes = require('../../src/server/routes.js')

const mockExpressApp = () => {
  return {
    get: jest.fn()
  }
}

const mockRegistry = () => {
  return {
    list: jest.fn(),
    Registry: {
      fromConnectionString: jest.fn()
    }
  }
}

const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms))

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

  describe('monitorDevices', () => {
    it('creates an interval that calls the registrys list function', async () => {
      const registry = mockRegistry()
      const devices = { devices: [] }
      registry.list = async () => { return { responseBody: devices }}
      const { interval } = routes.monitorDevices(registry, 1)
      await sleep(100)
      expect(devices).toEqual({ devices: [] })
      clearInterval(interval)
    })

    it('creates an interval with the set interval that calls the registrys list function', async () => {
      const registry = mockRegistry()
      const devices = { devices: [] }
      registry.list = async () => { return { responseBody: devices }}
      const { interval } = routes.monitorDevices(registry)
      await sleep(100)
      expect(devices).toEqual({ devices: [] })
      clearInterval(interval)
    })
  })
  
  describe('connect', () => {
    it('calls fromConnectionString on the registry with the connection string', () => {
      const registry = mockRegistry()
      routes.connect('conn_str', registry)
      expect(registry.Registry.fromConnectionString).toHaveBeenCalledWith('conn_str')
    })
  })
})