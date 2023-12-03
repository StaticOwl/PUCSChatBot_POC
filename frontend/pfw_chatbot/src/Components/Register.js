import { useState } from "react";
import { redirect } from "react-router-dom";
import "./Register.css";
const Register = (props) => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = (e) => {
    e.preventDefault();
    console.log(email);
    return redirect("/");
  };

  return (
    <>
      <div class="register-container">
        <h2>Register</h2>
        <form onSubmit={handleLogin} className="register-form">
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
          <br />
          <button type="submit"> Login </button>
        </form>
        <button onClick={() => props.onFormSwitch("login")}>
          Already have an account? Login here
        </button>
      </div>
    </>
  );
};

export default Register;
