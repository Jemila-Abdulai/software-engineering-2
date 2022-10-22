const azure = require('../../src/server/azure.js')

const mockRegistry = () => {
  return {
    list: jest.fn(),
    Registry: {
      fromConnectionString: jest.fn()
    }
  }
}

const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms))

describe('azure.js', () => {
  describe('monitorDevices', () => {
    it('creates an interval that calls the registrys list function', async () => {
      const registry = mockRegistry()
      const devices = { devices: [] }
      registry.list = async () => { return { responseBody: devices }}
      const { interval } = azure.monitorDevices(registry, 1)
      await sleep(100)
      expect(devices).toEqual({ devices: [] })
      clearInterval(interval)
    })

    it('creates an interval with the set interval that calls the registrys list function', async () => {
      const registry = mockRegistry()
      const devices = { devices: [] }
      registry.list = async () => { return { responseBody: devices }}
      const { interval } = azure.monitorDevices(registry)
      await sleep(100)
      expect(devices).toEqual({ devices: [] })
      clearInterval(interval)
    })
  })
  
  describe('connect', () => {
    it('calls fromConnectionString on the registry with the connection string', () => {
      const registry = mockRegistry()
      azure.connect('conn_str', registry)
      expect(registry.Registry.fromConnectionString).toHaveBeenCalledWith('conn_str')
    })
  })
})