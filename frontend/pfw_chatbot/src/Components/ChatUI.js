import React, { useState, useRef, useEffect } from "react";
import axios from "axios";
import "./ChatUI.css";

const ChatUI = () => {
  // Keep track of all messages
  const [messages, setMessages] = useState([
    { text: "Hello, how can I help you?", sender: "bot" },
    { text: "Hi there!", sender: "user" },
  ]);
  // Keep track of contents of input form
  const [newMessage, setNewMessage] = useState("");

  // Used to scroll down to last message
  const containerRef = useRef(null);
  useEffect(() => {
    if (containerRef && containerRef.current) {
      const element = containerRef.current;
      element.scroll({
        top: element.scrollHeight,
        left: 0,
        behavior: "smooth",
      });
    }
  }, [containerRef, messages]);

  // Handles appending of user input to chat followed by getting response from server
  const handleSendMessage = () => {
    if (newMessage.trim() === "") return;
    const updatedMessages = [
      ...messages,
      { text: newMessage, sender: "user" },
      // { text: "Standard response", sender: "bot" },
    ];
    setMessages(updatedMessages);
    setNewMessage("");
    //Receive reply from server
    axios.post('http://127.0.0.1:5000/v1/chatbot/chat', {
      user_msg: newMessage,
    })
    .then(function (res) {
      console.log(res);
      const updatedMessagesWithRes = [...messages, { text: newMessage, sender: 'user' },{ text: res.data.response, sender: 'bot' }];
      setMessages(updatedMessagesWithRes);
    })
    .then(function (err) {console.log(err);})
  };
  // Render the UI
  return (
    <div className="chat-ui">
      <div className="chat-window">
        <div className="messages-container" ref={containerRef}>
          {messages.map((message, index) => (
            <div className="message-box">
              <div
                className={`sender ${
                  message.sender === "user" ? "user" : "bot"
                }`}
              >
                <span className="sender-name">
                  {message.sender === "user" ? "User" : "PFW"}
                </span>
              </div>
              <div
                key={index}
                className={`message ${
                  message.sender === "user" ? "user" : "bot"
                }`}
              >
                {message.text}
              </div>
            </div>
          ))}
        </div>
      </div>
      <div className="input-box">
        <input
          className="input-form"
          type="text"
          placeholder="Type a message..."
          value={newMessage}
          onChange={(e) => setNewMessage(e.target.value)}
          onKeyPress={(e) => {
            if (e.key === "Enter") {
              handleSendMessage();
            }
          }}
        />
        <button className="send-btn" onClick={handleSendMessage}>
          Send
        </button>
      </div>
    </div>
  );
};

export default ChatUI;
