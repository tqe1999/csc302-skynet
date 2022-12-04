import React, { Component, useReducer } from 'react';
import { Button } from 'primereact/button';
import { Dropdown } from 'primereact/dropdown';

export class Stockbar extends Component {

    constructor(props) {
        super(props);
        this.state = {
            visibleLeft: true,
            stocksInPlay: 2,
            stocks: [],
            selectedStocks: []
        };
    }

    componentDidMount() {
        fetch("http://localhost:8000/stocks")
            .then(res => res.json())
            .then(stocks => this.setState({stocks}))
            .catch(error => console.error(error))
    }

    stockComponent() {
        const rows = [];
        const stockOptions = this.state.stocks.map(s => ({label: s, value: s}))

        for (let i = 0; i < this.state.selectedStocks.length; i++) {
            // note: we are adding a key prop here to allow react to uniquely identify each
            // element in this array. see: https://reactjs.org/docs/lists-and-keys.html
            rows.push(<div key={i} className='stockComponent'>
                <Dropdown value={this.state.selectedStocks[i]} options={stockOptions} placeholder="Select a Stock"/>
                <Button icon="pi pi-times" className="p-button-rounded p-button-danger p-button-text" aria-label="Cancel" onClick={
                    () => this.setState(state => ({selectedStocks: state.selectedStocks.filter((_, id) => id !== i)}))
                } />
            </div>);
        }

        return <div id="stockComponentsContainer">{rows}</div>
    }

    componentDidUpdate(_, prevState) {
        if (prevState.stocksInPlay !== this.state.stocksInPlay) {
            console.log(this.state.stocksInPlay)
        }

    }

    render() {
        return (
            <div id="sidebar">
                <h1>Stock Picker</h1>
                {this.stockComponent()}
                <Button label="Add Stock +" onClick={
                    () => this.setState(state => ({selectedStocks: [...state.selectedStocks, null]}))
                } />
            </div>
        );
    }
}
