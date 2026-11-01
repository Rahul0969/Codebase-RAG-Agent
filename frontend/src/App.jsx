import { useState } from 'react';

const API_URL = 'http://127.0.0.1:8000';

export default function App() {
  const [status, setStatus] = useState('Not checked');

  async function checkBackend() {
    try {
      const response = await fetch(`${API_URL}/health`);
      if (!response.ok) throw new Error('Backend request failed');
      const data = await response.json();
      setStatus(data.status === 'ok' ? 'Connected' : 'Unexpected response');
    } catch {
      setStatus('Backend unavailable');
    }
  }

  return (
    <main>
      <h1>Codebase RAG Assistant</h1>
      <p>Backend status: {status}</p>
      <button type="button" onClick={checkBackend}>Check backend</button>
    </main>
  );
}
