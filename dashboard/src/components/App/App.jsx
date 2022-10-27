import React from "react"
import Card from 'react-bootstrap/Card'

// The best way to write React applications is to split your App into separate components.
// I would recommend reading this https://reactjs.org/tutorial/tutorial.html#overview

export default class App extends React.Component {
    constructor() {
        super()
        this.state = {
            devices: []
        }
    }

    componentDidMount() {
        this.getDevices()
    }

    async getDevices() {
        const res = await fetch('/api/devices')
        const devices = await res.json()
        this.setState({ devices })
    }

    render() {
        const devices = this.state.devices
        return (
            <>
                {
                    devices.map(device =>
                        <Card style={{ width: '18rem' }} bg={device.alive ? 'success' : 'danger'} key={device.id}>
                            <Card.Body>
                                <Card.Text>{device.id}</Card.Text>
                            </Card.Body>
                        </Card>
                    )
                }
            </>

        )
    }
}