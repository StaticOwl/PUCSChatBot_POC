import { useState } from "react";
import "./App.css";
import Modal from "./Components/Modal";
import Navbar from "./Components/Navbar";

function App() {
  const [showModal, setShowModal] = useState(false)
  return (
    <div className="App">
      <Navbar></Navbar>
      <div className="content">
        <h1>PFW Computer Science Department</h1>
        <div>
          <p>Welcome to PFW, Computer Science Department! </p>
        </div>
      </div>
      <button className="ChatButton" onClick={() => {
        setShowModal(true);
      }}>Chat with us!</button>
      {showModal && <Modal hideModal={setShowModal} />}
    </div>
  );
}

export default App;
 