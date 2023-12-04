import { useState } from "react";
import axios from "axios";

import "./Register.css";
const Register = (props) => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const [error, setError] = useState("");
  const handleRegister = (e) => {
    e.preventDefault();
    if(name === '') setError("Name is empty!");
    else if (email === '') setError("Email is empty!");
    else if (password === '') setError("Password is empty!");
    else if (password !== confirmPassword) setError("Passwords do not match!");
    else{
        axios.post("http://127.0.0.1:5000/v1/app/register", {
        name: name,
        email: email,
        password: password
        }).then(
            function(res) {
                console.log("Registered successful!");
                props.onFormSwitch("login");
                setError("");
            }
        ).catch(
            function(error){
                console.log(error);
                setError("Invalid input details");
            }
        );
    }
    
  };

  return (
    <>
      <div className="register-container">
        <h2>Register</h2>
        <form onSubmit={handleRegister} className="register-form">
          <input
            type="text"
            id="name"
            value={name}
            placeholder="John Doe"
            onChange={(e) => setName(e.target.value)}
          />
          <br />
          <input
            type="email"
            id="email"
            value={email}
            placeholder="johndoe@example.com"
            onChange={(e) => setEmail(e.target.value)}
          />
          <br />
          <input
            type="password"
            id="passwd"
            value={password}
            placeholder="********"
            onChange={(e) => setPassword(e.target.value)}
          />
          <input
            type="password"
            id="passwd"
            value={confirmPassword}
            placeholder="Re-enter password"
            onChange={(e) => setConfirmPassword(e.target.value)}
          />
          <br />
          <p className="error">{error}</p>
          <button type="submit"> Register </button>
        </form>
        <button onClick={() => props.onFormSwitch("login")}>
          Already have an account? Login here
        </button>
      </div>
    </>
  );
};

export default Register;
