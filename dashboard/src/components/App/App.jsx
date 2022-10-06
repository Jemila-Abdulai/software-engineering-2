import React from "react"
import Button from 'react-bootstrap/Button'
import Card from 'react-bootstrap/Card'

// The best way to write React applications is to split your App into separate components.
// I would recommend reading this https://reactjs.org/tutorial/tutorial.html#overview

export default class App extends React.Component {
    constructor () {
        super()
        this.state = {
            devices: []
        }
    }

    componentDidMount () {
        this.getDevices()
    }

    async getDevices () {
        const res = await fetch('/api/devices')
        this.setState({ devices: await res.json() })
    }

    render () {
        const devices = this.state.devices
        return (
            <>
                { 
                    devices.map( device => 
                        <Card style={{ width: '18rem' }} bg={ device.alive ? 'success' : 'danger'}>
                            
                        <Card.Body>
                            <Card.Title> {device.device_name}</Card.Title>
                            <Card.Text>ID:{device.id}</Card.Text>
                        </Card.Body>
                        </Card> 
                    ) 
                    
                }
                
            </>
            
        )
    }
}