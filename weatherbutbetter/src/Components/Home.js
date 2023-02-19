import {
    Dropdown,
    DropdownToggle,
    DropdownMenu,
    DropdownItem,
    Label,
    Button,
} from "reactstrap";
import { Component } from 'react';
import React from 'react';
import '../App.css';
// 
// fetch("/", {
//       method: "POST",
//       headers: {"Content-Type": "application/JSON"},
//       body: JSON.stringify(newText) 
//     })
export default function Home(){
    const [data, setData] = React.useState(null);
    const [value, setValue] = React.useState('');

  React.useEffect(() => {
    fetch("/api")
      .then((res) => res.json())
      .then((data) => setData(data.message));
  }, []);
  console.log("data");
  console.log(data);
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("submitted");
    console.log(value);
    // uriContent = "data:application/octet-stream," + encodeURIComponent(content);
    // newWindow = window.open(uriContent, 'newDoc');
    // const fs = require('fs');
    // fs.writeData('C:\\Users\\jeeva\\OneDrive\\Documents\\Visual-Studio-Code-files\\Blueprint\\betterweather\\data.py', this.state.value, (e)=>{if(e){throw e;}});
//     fetch("/api", {
//   method: "POST",
//   headers: {"Content-Type": "application/JSON"},
//   body: JSON.stringify(newText) 
//     });
}
const handleInput = (e) => {
    // e.preventDefault();
    setValue(e.target.value);
}
return(
    <div>
    <h2 className="main-title">Just better weather</h2>
    {/* <link href = "https://code.jquery.com/ui/1.10.4/themes/ui-lightness/jquery-ui.css" rel = "stylesheet"/>
<script src = "https://code.jquery.com/jquery-1.10.2.js"></script>
<script src = "https://code.jquery.com/ui/1.10.4/jquery-ui.js"></script> */}
<form onSubmit={handleSubmit}>
<label>
    Location: {"   "}
    <input type="text" value={value} onChange={handleInput}/>
</label>
 <input type="submit" value="Submit" />
</form>
{/* <Button variant="primary">mary</Button> */}
    </div>
); 

}
// const root = ReactDOM.createRoot(document.getElementById('root'));
// const element = <Home />;
// root.render(element);

// export class Home extends Component {
//     constructor(props){
//         super(props);
//         this.state = {
//             value:  ""
//         };
//         this.handleInput = this.handleInput.bind(this);
//         this.handleSubmit = this.handleSubmit.bind(this);
//     }
//     // React.useEffect(() => {
//     //     fetch("/api")
//     //       .then((res) => res.json())
//     //       .then((data) => setData(data.message));
//     //   }, []);
//     handleSubmit = (e) => {
//         e.preventDefault();
//         console.log("submitted");
//         console.log(this.state.value);
//         // uriContent = "data:application/octet-stream," + encodeURIComponent(content);
//         // newWindow = window.open(uriContent, 'newDoc');
//         // const fs = require('fs');
//         // fs.writeData('C:\\Users\\jeeva\\OneDrive\\Documents\\Visual-Studio-Code-files\\Blueprint\\betterweather\\data.py', this.state.value, (e)=>{if(e){throw e;}});
//         fetch("/api", {
//       method: "POST",
//       headers: {"Content-Type": "application/JSON"},
//       body: JSON.stringify(newText) 
//         });
//     }
//     handleInput = (e) => {
//         // e.preventDefault();
//         this.setState({value: e.target.value});
//     }
//     render (){
//         return(
//             <div>
//             <h2 className="main-title">Just better weather</h2>
//             {/* <link href = "https://code.jquery.com/ui/1.10.4/themes/ui-lightness/jquery-ui.css" rel = "stylesheet"/>
//       <script src = "https://code.jquery.com/jquery-1.10.2.js"></script>
//       <script src = "https://code.jquery.com/ui/1.10.4/jquery-ui.js"></script> */}
//       <form onSubmit={this.handleSubmit}>
//         <label>
//             Location: {"   "}
//             <input type="text" value={this.state.value} onChange={this.handleInput}/>
//         </label>
//          <input type="submit" value="Submit" />
//         </form>
//         {/* <Button variant="primary">mary</Button> */}
//             </div>
//         ); 
//     }
// }
// const title = {
//     margin: "auto",
    
// }