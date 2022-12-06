import React, {Component, useState} from 'react';
import logo from './logo.svg';
import './App.css';
import { Button } from 'primereact/button';
import "primereact/resources/themes/lara-light-indigo/theme.css";  //theme
import "primereact/resources/primereact.min.css";                  //core css
import "primeicons/primeicons.css";                                //icons
import { Stockbar } from "./components/Stockbar"
import { Maindisplay } from "./components/Maindisplay"

const App = () => {
    const [selectedStocks, setSelectedStocks] = useState(null)

    return (
        <div className="App">
            <Stockbar setSelectedStocks={setSelectedStocks}/>
            <Maindisplay selectedStocks={selectedStocks}/>
        </div>
    )
}

export default App;
