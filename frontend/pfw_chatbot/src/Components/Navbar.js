import "./Navbar.css"

const Navbar = ({user}) => {
    console.log(user);
    function handleLogout(){
        user = {name: '', email: '', logged_in: false};
        localStorage.setItem("user", JSON.stringify(user));
        // document.cookie = "user=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
        window.location.reload();
    }
    return ( 
        <nav className="navbar" style={{display:"flex", backgroundColor:"black", color:"white"}}>
            <div style={{padding:'10px', marginLeft: '50px'}}><h1>PFW</h1></div>
            <div style={{marginLeft:'auto'}}>
                {user.logged_in && <button className="logout-button" onClick={handleLogout}>Logout</button>}
            </div>
        </nav>
     );
}
 
export default Navbar;