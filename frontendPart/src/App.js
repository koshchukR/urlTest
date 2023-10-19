import './App.css';
import Form from "./components/Form";
import {createBrowserRouter, RouterProvider} from "react-router-dom";
import React from "react";
import LoginScreen from "./components/LoginScreen";
import RegisterScreen from "./components/RegisterScreen";

function App() {
    const router = createBrowserRouter([
        {
            path: "/",
            element: <Form/>,
        },
        {
            path: "/login",
            element: <LoginScreen/>,
        },
        {
            path: "/register",
            element: <RegisterScreen/>
        }
    ]);
    return (
        <div className="App">
            <RouterProvider router={router}/>
        </div>
    );
}

export default App;
