import { useEffect, useState } from "react";
import "./App.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Login from "./Components/Login";
import Register from "./Components/Register";
import Navbar from "./Components/Navbar";
import Home from "./Components/Home";

function App() {
  const [user, setUser] = useState(
    {name:'', email:'', logged_in:false}
  );
  useEffect(()=> {
    const get_user = JSON.parse(localStorage.getItem("user"));
    if(get_user) setUser(get_user);
  }, []);
  console.log("User:");
  console.log(user);
  const [currentForm, setCurrentForm] = useState("login");
  // const []
  const toggleForm = (formName) => {
    setCurrentForm(formName);
  };
  return (
    <div className="App">
      <Navbar user={user}></Navbar>
      <div className="container">
        {!user.logged_in &&
          (currentForm === "login" ? (
            <Login onFormSwitch={toggleForm} />
          ) : (
            <Register onFormSwitch={toggleForm} />
          ))}
        {user.logged_in && (
          <BrowserRouter>
            <Routes>
              <Route path="/">
                <Route index element={<Home />}></Route>
              </Route>
            </Routes>
          </BrowserRouter>
        )}
      </div>
    </div>
  );
}

export default App;
