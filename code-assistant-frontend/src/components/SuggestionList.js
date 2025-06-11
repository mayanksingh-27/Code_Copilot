import React from 'react';

function SuggestionList({ suggestions = [] }) {
  return (
    <ul>
      {suggestions.length === 0 ? (
        <li>No suggestions yet</li>
      ) : (
        suggestions.map((sug, index) => (
          <li key={index}>
            <strong>{sug.token}</strong> ({(sug.probability * 100).toFixed(2)}%)
          </li>
        ))
      )}
    </ul>
  );
}

export default SuggestionList;