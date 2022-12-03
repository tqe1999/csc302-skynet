import React, { Component, useReducer } from 'react';
import { Button } from 'primereact/button';
import { Dropdown } from 'primereact/dropdown';

export class Stockbar extends Component {

    constructor(props) {
        super(props);
        this.state = {
            visibleLeft: true,
            stocksInPlay: 2
        };
    }

    stockComponent() {
        const rows = [];

        for (let i = 0; i < this.state.stocksInPlay; i++) {
            // note: we are adding a key prop here to allow react to uniquely identify each
            // element in this array. see: https://reactjs.org/docs/lists-and-keys.html
            rows.push(<div key={i} className='stockComponent'>
                <Dropdown value={this.state.selectedCountry} options={this.countries} onChange={this.onCountryChange} optionLabel="name" filter showClear filterBy="name" placeholder="Select a Stock"
                    valueTemplate={this.selectedCountryTemplate} itemTemplate={this.countryOptionTemplate} />
                <Button icon="pi pi-times" className="p-button-rounded p-button-danger p-button-text" aria-label="Cancel" onClick={
                    () => this.setState(state => { return { stocksInPlay: state.stocksInPlay - 1 } })
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
                    () => this.setState(state => { return { stocksInPlay: state.stocksInPlay + 1 } })
                } />
            </div>
        );
    }
}
