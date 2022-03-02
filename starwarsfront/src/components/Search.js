import {useState} from "react";
import ShowCharacters from './ShowCharacters'
import ShowFilms from './ShowFilms'

function Search(props) {
    const filteredData = ShowCharacters.filter((el) => {
        if (props.input === '') {
            return el;
        } else {
            return el.text.toLowerCase().includes(props.input)
        }
    })
    return (
        <ul>
            {filteredData.map((item) => (
                <li key={item.name}>{item.hair_color}{item.title}{item.director}
                </li>
            ))}
        </ul>
    )
}

export default Search


import { React, useState } from "react";
import TextField from "@mui/material/TextField";
import ReactDOM from 'react-dom';
import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css'
import {Route, Routes } from 'react-router-dom';
import ShowFilms from './components/ShowFilms'
import ShowCharacters from './components/ShowCharacters'
import CharacterDetail from './components/CharacterDetail';
import ShowSpecies from './components/ShowSpecies';
import ShowPlanets from './components/ShowPlanets';
import Starships from './components/Starships';
import NavbarMenu from './components/Navbar';
import Search from "./Components/Search";

function Home() {
  const [inputText, setInputText] = useState("");
  let inputHandler = (e) => {
    //convert input text to lower case
    var lowerCase = e.target.value.toLowerCase();
    setInputText(lowerCase);
  }
  return (
    
    
    <div className="App"> 
      <h1>Search</h1>
      <div className="search">
        <TextField
          id="outlined-basic"
          onChange={inputHandler}
          variant="outlined"
          fullWidth
          label="Search"
        />
      </div>
      <Search input={inputText} />

      <NavbarMenu />
      <Routes>      
        <Route path="/films" element={<ShowFilms />} />
        <Route path="/characters" element={<ShowCharacters />} />  
        <Route path="/:id/" element={<CharacterDetail />} />
        <Route path="/species" element={<ShowSpecies />} />
        <Route path="/planets" element={<ShowPlanets />} /> 
        <Route path="/starships" element={<Starships />} /> 
        
      </Routes>
      
      
      
      
      
        
    </div>
    
    
    
  )
}
export default App;

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
