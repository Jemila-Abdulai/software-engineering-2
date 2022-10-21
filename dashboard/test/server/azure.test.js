const { IoTHubTokenCredentials } = require('azure-iothub')
const azure = require('../../src/server/azure.js')

const mockRegistry = overrideFunctions => {
  return {
    list: overrideFunctions.list || jest.fn(),
    Registry: {
      fromConnectionString: overrideFunctions
    }
  }
}

describe('azure.js', () => {
  describe('monitorDevices', () => {
    it('creates an interval wih the set poll time', () => {
      
    })
  })
})