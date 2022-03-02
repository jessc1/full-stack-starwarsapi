import axios from "axios";
import React, {useState, useEffect} from 'react';
import { Card, Button } from 'react-bootstrap'
import { Link } from 'react-router-dom';



const ShowCharacters = () => {
  const [characters, setCharacters] = useState([])
  const getCharacters = async () => {
    const response = await axios.get("http://localhost:8000/starwars/character/list")
    setCharacters(response.data)
  }
  useEffect(() => {
    getCharacters();
  }, [])

  return (
    <div>
      <h1>All Star Wars Characters</h1>
      { 
      
        characters.map((character, index) => (
          <Card className="m-3 rounded shadow-lg main-films-show" style={{ width: '22rem' }}>
        
          <Card.Body>
            <Card.Title>{character.name}</Card.Title>
            <Card.Text>{character.hair_color}</Card.Text>        
          
            <Link className="btn btn-primary mr-2" to={`/${character.id}`}>Full Detail</Link>
          </Card.Body>
          </Card>
        ))
      }
    </div>

  );
};

export default ShowCharacters;