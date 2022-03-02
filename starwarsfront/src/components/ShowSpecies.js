import axios from "axios";
import React, {useState, useEffect} from 'react';
import { Card, Button } from 'react-bootstrap'
import { Link } from 'react-router-dom';



const ShowSpecies = () => {
  const [species, setSpecies] = useState([])
  const getSpecies = async () => {
    const response = await axios.get("http://localhost:8000/starwars/species")
    setSpecies(response.data)
  }
  useEffect(() => {
    getSpecies();
  }, [])

  return (
    <div>
      <h1>Species</h1>
      { 
      
        species.map((specie, index) => (
          <Card className="m-3 rounded shadow-lg main-films-show" style={{ width: '22rem' }}>
        
          <Card.Body>
            <Card.Title>Name: {specie.name}</Card.Title>
            <Card.Text>Language: {specie.language}</Card.Text>        
          
            <Link className="btn btn-primary mr-2" to={`/${specie.id}`}>Full Detail</Link>
          </Card.Body>
          </Card>
        ))
      }
    </div>

  );
};

export default ShowSpecies;