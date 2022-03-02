import React from 'react';
import {useState, useEffect} from "react";
import axios from "axios";
import List from "./List"




function ShowFilms() {
  const [isExpanded, setExpanded]= useState(false)
  const [rows, setRows]= useState(1)

  const [films , setNewFilms] = useState(null)
  const [formFilm, setFormFilm] = useState({
        title: "",
        episode_id: "",
        opening_crawl: "",
        director: "",
        producer: "",
        release_date: "",
        characters: "",
        planets: "",
        starships: "",
        vehicles: "",
        species: "",
        created: "",
        edited: "",
        url: ""
        })

      useEffect(() => {
          getFilms()
            } ,[])
      
      function getFilms() {
          axios({
              method: "GET",
              url:"http://localhost:8000/starwars/film/list",
                }).then((response)=>{
                  const data = response.data
                  setNewFilms(data)
                }).catch((error) => {
                  if (error.response) {
                    console.log(error.response);
                    console.log(error.response.status);
                    console.log(error.response.headers);
                    }
                })}
      

      function DeleteFilm(id) {
          axios({
            method: "DELETE",
            url:`/starwars/${id}/`,
          })
          .then((response) => {
            getFilms()
          })
      }

      function handleChange(event) { 
          const {value, name} = event.target
          setFormFilm(prevFilm => ({
              ...prevFilm, [name]: value})
          )}
      function FilmShow(){
          setExpanded(true)
          setRows(3)
          }
    

      

    return (

     <div className=''>

        

        { films && films.map(film => <List
        key={film.id}
        id={film.id}
        title={film.title}
        episode_id ={film.episode_id}
        opening_crawl={film.opening_crawl}
        director= {film.director}
        producer={film.producer}
        release_date={film.release_date}
        characters={film.characters}
        planets={film.planets}
        starships={ film.starships}
        vehicles={ film.vehicles}
        species={ film.species}
        created= {film.created}
        edited={ film.edited}
        url={film.url}
            
        
        deletion ={DeleteFilm}
        />
        )}

    </div>

  );
}

export default ShowFilms;




