import axios from "axios";
import React, {useState, useEffect} from 'react';
import { Card, Button } from 'react-bootstrap'
import { Link } from 'react-router-dom';



const Starships = () => {
  const [starships, setStarships] = useState([])
  const getStarships = async () => {
    const response = await axios.get("http://localhost:8000/starwars/starships")
    setStarships(response.data)
  }
  useEffect(() => {
    getStarships();
  }, [])

  return (
    <div>
      <h1>Starships</h1>
      { 
      
        starships.map((starship, index) => (
          <Card className="m-3 rounded shadow-lg main-films-show" style={{ width: '22rem' }}>
        
          <Card.Body>
            <Card.Title>Hyperdrive Rating: {starship.hyperdrive_rating}</Card.Title>
            <Card.Text>Starship Class: {starship.starship_class}</Card.Text>
            
            <Link className="btn btn-primary mr-2" to={`/${starship.id}`}>More Details</Link>
          </Card.Body>
          </Card>
        ))
      }
    </div>

  );
};

export default Starships;