import axios from "axios";
import React, {useState, useEffect} from 'react';
import { Card, Button } from 'react-bootstrap'
import { Link } from 'react-router-dom';



const ShowPlanets = () => {
  const [planets, setPlanets] = useState([])
  const getPlanets = async () => {
    const response = await axios.get("http://localhost:8000/starwars/planets")
    setPlanets(response.data)
  }
  useEffect(() => {
    getPlanets();
  }, [])

  return (
    <div>
      <h1>Planets</h1>
      { 
      
        planets.map((planet, index) => (
          <Card className="m-3 rounded shadow-lg main-films-show" style={{ width: '22rem' }}>
        
          <Card.Body>
            <Card.Title>Name: {planet.name}</Card.Title>
            <Card.Text>Climate: {planet.climate}</Card.Text>
            <Card.Text>Orbital Period: {planet.orbital_period}</Card.Text>        
          
            <Link className="btn btn-primary mr-2" to={`/${planet.id}`}>More Details</Link>
          </Card.Body>
          </Card>
        ))
      }
    </div>

  );
};

export default ShowPlanets;