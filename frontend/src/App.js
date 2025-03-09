import logo from './logo.svg';
import { useState, useEffect } from "react";
import './App.css';
import Header from './header';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

function DataFetcher() {
  const [data, setData] = useState([]);
  const [selectedParts, setSelectedParts] = useState(new Set());

  useEffect(() => {
    fetch("http://127.0.0.1:8000/parts/")
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      setData(data);
    })
    .catch((error) => console.error("Error fetching data:", error));
  }, []);

  const handleCheckboxChange = (id) => {
    setSelectedParts((prevSelected) => {
      const newSelected = new Set(prevSelected);
      if (newSelected.has(id)) {
        newSelected.delete(id);
      } else {
        newSelected.add(id);
      }
      console.log("Selected Parts:", [...newSelected]);
      return newSelected;
    });
  };
  

  return (
    <ul>
      {data.map((part) => (
        <li key={part.id}>
          <input
            type="checkbox"
            onChange={() => handleCheckboxChange(part.id)}
          />
            {part.name} - ${part.price}
        </li>
      ))}
    </ul>
  );
}




function App() {
  return (
    <div className="App">
        <Header />
        {/* <img src={logo} className="App-logo" alt="logo" /> */}
        <DataFetcher />
    </div>
  );
}

export default App;
