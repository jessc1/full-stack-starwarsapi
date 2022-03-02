import React  from 'react';
import {useState, useEffect} from "react";
import axios from "axios";
import ShowCharacters from './ShowCharacters'

const  Home = () => {
  const [query, setQuery] = useState("");
  const [characters, setCharacters] = useState([]);

  useEffect(() => {
    const searchCharacter = async () => {
      const res = await axios.get(`http://127.0.0.1:8000/starwars/character/list${query}`);
      setCharacters(res.characters);
    };
    if (query.length === 0 || query.length > 2) searchCharacter();
  }, [query]);
    return (
        <div>
          <section>
            <h1>Welcome to Star Wars API</h1>
            <p>This is where the fun begins</p>
          </section>
          <div className="app">
        <input
          className="search"
          placeholder="Search in the star wars API..."
          onChange={(e) => setQuery(e.target.value.toLowerCase())}
        />
      {<ShowCharacters characters={characters} />}
    </div>
  );


      </div>
    );

};
    


export default Home;



