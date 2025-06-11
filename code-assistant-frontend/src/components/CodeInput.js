import React from 'react';

function CodeInput({ code, setCode, onSubmit }) {
  return (
    <div>
      <textarea
        value={code}
        onChange={(e) => setCode(e.target.value)}
        placeholder="Type your code..."
        rows={8}
        cols={60}
      />
      <br />
      <button onClick={onSubmit}>Autocomplete</button>
    </div>
  );
}

export default CodeInput;