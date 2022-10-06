import React from "react";
import Enzyme, { shallow } from 'enzyme'
import Adapter from 'enzyme-adapter-react-16';

// Good devs test their code :)
// This uses Enzyme to render our React components and it puts them in a nice wrapper
// to make testing them easy

import App from '../src/frontend/components/App/App.jsx'

Enzyme.configure({ adapter: new Adapter() });

describe('App', () => {
    test('displays a paragraph', () => {
        const app = shallow(<App />)
        const parahraph = app.find('p')
        expect(parahraph).toHaveLength(1)
    })
})