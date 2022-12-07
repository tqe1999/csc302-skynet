import React, { Component } from 'react';
import { Image } from "primereact/image"
export class Maindisplay extends Component {

    constructor(props) {
        super(props);
        this.state = {
            visibleLeft: true,
            image: null
        };
    }

    componentDidUpdate(prevProps) {
        if (prevProps.selectedStocks !== this.props.selectedStocks && this.props.selectedStocks) {
            const form = new FormData()
            form.append("stocks", JSON.stringify(this.props.selectedStocks))
            fetch("http://localhost:8000/correlation/", {
                method: "POST",
                body: form
            })
                .then(res => res.blob())
                .then(blob => {
                    const reader = new FileReader()
                    reader.onload = () => this.setState({ image: reader.result })
                    reader.readAsDataURL(blob)
                })
        }
    }

    render() {
        if (this.state.image) {
            return (
                <div id="maindisplay">
                    <Image src={this.state.image} />
                </div>
            )
        }
        return (
            <div id="maindisplay">
                <i className="pi pi-arrow-left" style={{ 'fontSize': '2em' }}></i>
                <h2>Select at least 2 stocks to get started</h2>
            </div>
        );
    }
}
