import { useState } from "react";
import "./App.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Login from "./Components/Login";
import Register from "./Components/Register";
import Navbar from "./Components/Navbar";
import Home from "./Components/Home";

function App() {
  const [user, setUser] = useState(
    JSON.parse(localStorage.getItem("user")) || {
      logged_in: false,
      user: "",
      email: "",
    }
  );
  console.log("User:");
  console.log(user);
  const [currentForm, setCurrentForm] = useState("login");
  // const []
  const toggleForm = (formName) => {
    setCurrentForm(formName);
  };
  return (
    <div className="App">
      <Navbar></Navbar>
      <div className="container">
        {!user.logged_in &&
          (currentForm === "login" ? (
            <Login handler={setUser} onFormSwitch={toggleForm} />
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
