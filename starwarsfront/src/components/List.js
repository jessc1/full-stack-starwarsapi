function List(props){
    function handleClick(){
  props.deletion(props.id)
}
  return (
      <div className="films">
        <h1 >Title: {props.title} </h1>        
        <p> episode_id: {props.episode_id}</p>
        <p> opening_crawl:{props.opening_crawl}</p>
        <p> director: {props.director}</p>
        <p> producer: {props.producer}</p>
        <p> release_date: {props.release_date}</p>
        <p> characters: {props.characters}</p>
        <p> planets: {props.planets}</p>
        <p> starships: {props.starships}</p>
        <p> vehicles: {props.vehicles}</p>
        <p> species: {props.species}</p>
        <p> created: {props.created}</p>
        <p> edited: {props.edited}</p>
        <p> url: {props.url}</p>
        
        <button onClick={handleClick}>Delete</button>
      </div>
  )
}

export default List;