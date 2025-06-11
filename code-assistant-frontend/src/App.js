import React, { useState } from 'react';
import Header from './components/Header';
import CodeInput from './components/CodeInput';
import SuggestionList from './components/SuggestionList';
import './App.css'; 

function App() {
  const [code, setCode] = useState('');
  const [suggestions, setSuggestions] = useState([]);

  const handleAutocomplete = async () => {
    const response = await fetch('http://localhost:8080/api/autocomplete', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ code }),
    });

    const data = await response.json();
    setSuggestions(data.suggestions);
  };

  return (
    <div style={{ padding: '2rem' }}>
      <Header />
      <CodeInput code={code} setCode={setCode} onSubmit={handleAutocomplete} />
      <h2>Suggestions:</h2>
      <SuggestionList suggestions={suggestions} />
    </div>
  );
}

export default App;