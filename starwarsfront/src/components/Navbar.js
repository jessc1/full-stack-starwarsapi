import React from 'react'
import { Navbar, Nav, Container } from 'react-bootstrap';
import {BrowserRouter, Routes, Route, Link, NavLink } from 'react-router-dom';


const NavbarMenu = () => {
  return (
    <Navbar bg="dark" variant="dark">
    <Container>
    <Navbar.Brand as={Link} to="/">Star Wars </Navbar.Brand>
    <Nav className="me-auto">
      <Nav.Link as={Link} to="/home">Home</Nav.Link>   
      <Nav.Link as={Link} to="/films">Films</Nav.Link>
      <Nav.Link as={Link}to="/characters">Characters</Nav.Link>
      <Nav.Link as={Link}to="/species">Species</Nav.Link>
      <Nav.Link as={Link}to="/starships">Starships</Nav.Link>
      <Nav.Link as={Link}to="/planets">Planets</Nav.Link>
    </Nav>
    </Container>
  </Navbar>
  
 

      
  )
}

export default NavbarMenu;