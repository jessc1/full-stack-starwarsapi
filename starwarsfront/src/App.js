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
import Home from './components/Home';

function App() {
  
  return (
    
    
    <div className="App">    
      

      <NavbarMenu />
      <Routes>
        <Route path="/home" element={<Home />} />
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
