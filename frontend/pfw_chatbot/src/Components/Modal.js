import ChatUI from "./ChatUI";
import './Modal.css'

function Modal({hideModal}) {
  return (
    <div className="modal">
      <div className="ChatBox">
        <div className="title">
          <span className="close" onClick={() => {hideModal(false)}}>&times;</span>
        </div>
        <div className="body">
          <ChatUI></ChatUI>
        </div>
      </div>
    </div>
  );
}

export default Modal;
