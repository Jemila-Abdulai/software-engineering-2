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
  })
})