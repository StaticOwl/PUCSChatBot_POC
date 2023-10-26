import './App.css';
import ChatUI from './ChatUI';
import Navbar from './Navbar'

function App() {
  return (
    <div className="App">
      <Navbar></Navbar>
      <div className="content">
        <h1>PFW Computer Science Department</h1>
        <div>
          <p>Welcome to PFW, Computer Science Department! </p>
        </div>
      </div>
      <div className="ChatBox">
        <ChatUI></ChatUI>
      </div>
    </div>
  );
}

export default App;
