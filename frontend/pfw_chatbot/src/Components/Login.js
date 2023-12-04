import axios from "axios";
import React, {useState} from "react";
import "./Login.css"

const Login = (props) => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const handleLogin = (e) => {
        e.preventDefault();
        console.log(email);
        axios.post('http://127.0.0.1:5000/v1/app/login', {
            email:email, 
            password:password,
            is_guest:false
        }).then(function (res) {
            console.log("Success!");
            console.log(res);
            const user = {name: res.name, email: res.email, logged_in: true};
            localStorage.setItem("user", JSON.stringify(user));
            setError("");
            window.location.reload();
        }).catch(function(err) {
            console.log(err);
            setError("Incorrect username or password!");
        });
    }

    const handleGuestLogin = (e) => {
        e.preventDefault();
        // console.log(email);
        axios.post('http://127.0.0.1:5000/v1/app/login', {
            email:email, 
            password:password,
            is_guest:true
        }).then(function (res) {
            const user = {name: res.name, email: res.email, logged_in: true};
            console.log(user);
            localStorage.setItem('user', JSON.stringify(user));
            window.location.reload();
        }).catch(function(err) {
            console.log(err);
            setError("Incorrect username or password");
        });;
    }
    return (
        <>
        <div className="login-container">
            <h2>Login</h2>
            <form onSubmit={handleLogin} className="login-form">
                <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="johndoe@example.com"/>
                <br />
                <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder = "*******"/>
                <br />
                <p className="error">{error}</p>
                <br />
                <button type="submit"> Login </button>
                <br></br>
                
                <button type="button" onClick={handleGuestLogin}> Login as guest?</button>
            </form>
            <button onClick={() => props.onFormSwitch('register')}>Don't have an account? Register here</button>
        </div>
        </>
    );
}

export default Login