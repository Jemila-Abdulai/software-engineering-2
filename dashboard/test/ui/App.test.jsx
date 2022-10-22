import React from "react"
import Enzyme, { mount } from 'enzyme'
import Adapter from 'enzyme-adapter-react-16'
import Card from 'react-bootstrap/Card'

import App from '../../src/components/App/App.jsx'

Enzyme.configure({ adapter: new Adapter() })

export const sleep = milliseconds => new Promise(resolve => {
    setTimeout(() => {
        resolve()
    }, milliseconds)
})

describe('App', () => {
    beforeEach(() => {
        fetch.resetMocks()
    })

    test('renders a card for each sensor', async () => {
        // getting enzyme to wait for an API call is a pain in the ass
        const mockData = [
            { id: 5673, device_name: 'soil_sensor_1', alive: true },
            { id: 5612, device_name: 'soil_sensor_2', alive: true },
            { id: 5243, device_name: 'soil_sensor_3', alive: false }
        ]
        fetch.mockResponse(async req => {
            if (req.url.match('/api/devices')) {
                return JSON.stringify(mockData)
            }
            throw Error(`Unexpected API call: ${req.url}`)
        })
        const mounted = mount(<App />)
        expect(fetch.mock.calls).toEqual([
            ['/api/devices']
        ])

        // this shouldn't be here, there is no other way
        await sleep(10)

        mounted.update()
        expect(mounted.find(Card)).toHaveLength(mockData.length)
    })
})