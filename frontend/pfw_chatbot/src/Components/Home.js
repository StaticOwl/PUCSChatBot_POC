import { useState } from "react";
import Modal from "./Modal";

const Home = (props) => {
  const [showModal, setShowModal] = useState(false);
  console.log( props.user);

  return (
    <>
      <h1>PFW Computer Science Department</h1>
      <div>
        <p>Welcome to PFW, Computer Science Department! </p>
      </div>

      <button
        className="ChatButton"
        onClick={() => {
          setShowModal(true);
        }}
      >
        Chat with us!
      </button>
      {showModal && <Modal hideModal={setShowModal} />}
    </>
  );
};

export default Home;
