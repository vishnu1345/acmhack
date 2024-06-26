import React from 'react'
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom"
import LandingPage from './components/LandingPage';
// import Map from "./components/Map"
import LoginPage from './components/LoginPage';
import RegisterPage from './components/RegisterPage'
import Home from './components/Home';
import Vishnu from './components/Vishnu';
// import MapSec from "./components/MapSec"
// import Floating from './components/Floating';
function App() {
  const router  = createBrowserRouter([
    {
      path: "/",
      element:<LandingPage/>
      // element:<MapSec/>

    },
    {
      path: "/login",
      element:<LoginPage/>
    },
    {
      path: "/register",
      element:<RegisterPage/>
    },
    {
      path: "/home",
      element:<Home/>
    },
    {
      path: "/vishnu",
      element:<Vishnu/>
    }
    
  ]);
  return (
    <div>
      <RouterProvider router = {router}/>
    </div>
  )
}

export default App
