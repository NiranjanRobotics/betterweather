import {
    Dropdown,
    DropdownToggle,
    DropdownMenu,
    DropdownItem,
    Label,
    Button,
} from "reactstrap";
import React, { Component } from 'react'
import '../App.css';
// import fs from "fs";


export class Home extends Component {
    constructor(props){
        super(props);
        this.state = {
            value:  ""
        };
        this.handleInput = this.handleInput.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    handleSubmit = (e) => {
        e.preventDefault();
        console.log("submitted");
        console.log(this.state.value);
        // uriContent = "data:application/octet-stream," + encodeURIComponent(content);
        // newWindow = window.open(uriContent, 'newDoc');
        // const fs = require('fs');
        // fs.writeData('C:\\Users\\jeeva\\OneDrive\\Documents\\Visual-Studio-Code-files\\Blueprint\\betterweather\\data.py', this.state.value, (e)=>{if(e){throw e;}});
    }
    handleInput = (e) => {
        // e.preventDefault();
        this.setState({value: e.target.value});
    }
    render (){
        return(
            <div>
            <h2 className="main-title">Just better weather</h2>
            {/* <link href = "https://code.jquery.com/ui/1.10.4/themes/ui-lightness/jquery-ui.css" rel = "stylesheet"/>
      <script src = "https://code.jquery.com/jquery-1.10.2.js"></script>
      <script src = "https://code.jquery.com/ui/1.10.4/jquery-ui.js"></script> */}
      <form onSubmit={this.handleSubmit}>
        <label>
            Location: {"   "}
            <input type="text" value={this.state.value} onChange={this.handleInput}/>
        </label>
         <input type="submit" value="Submit" />
        </form>
        {/* <Button variant="primary">mary</Button> */}
            </div>
        ); 
    }
}
const title = {
    margin: "auto",
    
}