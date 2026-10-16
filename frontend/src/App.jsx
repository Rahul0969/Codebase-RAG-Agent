import { useState } from 'react';
import "./style.css"

function App() {
  const [status, setStatus] = useState("Not Checked");

  async function checkBackend() {
    try{
      const response = await fetch("http://127.0.0.1:8000/health");
      const data = await response.json();

      setStatus(data.status === "ok" ? "Connected" : "Error");
    }catch{
      setStatus("Backend unavailable");
    }
  }

  return(
    <main>
      <h1>CodeBase RAG Agent:</h1>
      <p>Backend status : {status}</p>
      <button onClick = {checkBackend}>
        Check backend
      </button>
    </main>
  );
}

export default App;