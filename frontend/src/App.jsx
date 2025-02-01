import { useState } from 'react'
import './App.css'
import logo from './assets/logo.png'
import Search from './components/Search/Search'
import Suggest from './components/Suggest/Suggest'


function App() {

  return (
    <div className='container'>
      <div className="overlay"></div> 
      <div className="header">
        <img src={logo} alt="hitbox logo" />
        <p>Hitbox</p>
      </div>
      <div className='body-text'>
        <p>Hello there,</p>
        <h3>What would you like to play today</h3>
        <Search />
        <div className='suggestions'>
          <Suggest text="Action games released after 2010"/>
          <Suggest text="Action games released after 2010"/>
          <Suggest text="Action games released after 2010"/>
          <Suggest text="Action games released after 2010"/>
          <Suggest text="Action games released after 2010"/>
          <Suggest text="Action games released after 2010"/>

          
        </div>
      </div>
      <div className='search-container'>
        
        
      </div>
    </div>
  )
}

export default App
