import React from "react"

// The best way to write React applications is to split your App into separate components.
// I would recommend reading this https://reactjs.org/tutorial/tutorial.html#overview

export default class App extends React.Component {
    constructor () {
        super()
        this.state = {
            text: ''
        }
    }

    componentDidMount () {
        this.getText()
    }

    async getText () {
        const res = await fetch('/api/hello')
        this.setState({ text: await res.json() })
    }

    render () {
        return (
            <p>{this.state.text}</p>
        )
    }
}