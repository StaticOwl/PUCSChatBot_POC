import { useState } from "react";
import axios from "axios";

import "./Register.css";
const Register = (props) => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleRegister = (e) => {
    e.preventDefault();
    axios.post("http://127.0.0.1:5000/v1/app/register", {
      name: name,
      email: email,
      password: password
    }).then(
        function(res) {
            console.log("Registered successful!");
            props.onFormSwitch("login");
        }
    );
    
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
            value={password}
            placeholder="Re-enter password"
            onChange={(e) => setPassword(e.target.value)}
          />
          <br />
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
