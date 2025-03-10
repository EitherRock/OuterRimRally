import { useState, useEffect } from "react";


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