import React, { Component } from 'react';
import { Sidebar } from 'primereact/sidebar';
export class Maindisplay extends Component {

    constructor(props) {
        super(props);
        this.state = {
            visibleLeft: true,
        };
    }

    render() {
        return (
            <div id="maindisplay">
                <i className="pi pi-arrow-left" style={{ 'fontSize': '2em' }}></i>
                Select at least 2 stocks to get started
            </div>
        );
    }
}
