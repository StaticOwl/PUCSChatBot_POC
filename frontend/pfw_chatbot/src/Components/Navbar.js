import { useEffect, useRef } from "react";
import "./Navbar.css"

const Navbar = () => {
    var user = JSON.parse(localStorage.getItem('user'));
    var showLogoutButton = useRef(user['logged_in']);
    console.log(showLogoutButton);
    useEffect(()=> {
        
        showLogoutButton.current = user['logged_in'];
    }, [user]);
    function handleLogout(){
        user = {'user': '', 'email': '', 'logged_in': false};
        localStorage.setItem('user', JSON.stringify(user));
        // document.cookie = "user=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
        window.location.reload();

    }
    return ( 
        <nav className="navbar" style={{display:"flex", backgroundColor:"black", color:"white"}}>
            <div style={{padding:'10px', marginLeft: '50px'}}><h1>PFW</h1></div>
            <div style={{marginLeft:'auto'}}>
                {showLogoutButton.current && <button className="logout-button" onClick={handleLogout}>Logout</button>}
            </div>
        </nav>
     );
}
 
export default Navbar;