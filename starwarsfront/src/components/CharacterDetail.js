import axios from 'axios';
import React, {useEffect, useState} from 'react';
import {Card, Button} from 'react-bootstrap';
import { useParams, useNavigate} from 'react-router';
import { Link } from 'react-router-dom';

const CharacterDetail = () => {
    const [character, setCharacter] = useState([])
    const{id} = useParams();
    const history = useNavigate();



useEffect(() => {
    getSingleCharacter();
}, [])

const getSingleCharacter = async () => {
    const { data } = await axios.get(`http://localhost:8000/starwars/character/${id}`)
    console.log(data);
    setCharacter(data);
}

const deleteCharacter = async (id) => {
    await axios.get(`http://localhost:8000/starwars/character/${id}`)
    history.push("/")

}



return (
    <div>
        <h2>Detail of Single Character </h2>
        <hr></hr>
        <div className="full-character-detail">
            
            <div className="character-detail">
                <p>Id: {character.id}</p>
                <p>Name: {character.name}</p>
                <p>Height: {character.height}</p>
                <p>Mass: {character.mass}</p>
                <p>Hair Color: {character.hair_color}</p>
                <p>Skin Color: {character.skin_color}</p>
                <p>Eye Color: {character.eye_color}</p>
                <p>Birth Year: {character.birth_year}</p>                           
                
            </div>           

        </div>
        
        
    </div>
);

};

export default CharacterDetail;