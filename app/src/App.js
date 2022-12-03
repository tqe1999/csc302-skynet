import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import { Button } from 'primereact/button';
import "primereact/resources/themes/lara-light-indigo/theme.css";  //theme
import "primereact/resources/primereact.min.css";                  //core css
import "primeicons/primeicons.css";                                //icons
import { Stockbar } from "./components/Stockbar"
import { Maindisplay } from "./components/Maindisplay"

class App extends Component {
  render() {
    return (
      <div className="App" >
        <Stockbar />
        <Maindisplay />
      </div >
    );
  }
}

export default App;
