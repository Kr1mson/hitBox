import React, { useState } from 'react';
import './Search.css';

const Search = () => {
  const [query, setQuery] = useState('');

  const handleSearch = async () => {
    if (!query.trim()) return; // Prevent empty queries

    const requestData = {
      query: query,
      top_n: 5,
    };

    try {
      const response = await fetch('http://127.0.0.1:5000/recommend', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestData),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      console.log('Recommended Games:', data);
    } catch (error) {
      console.error('Error fetching recommendations:', error);
    }
  };

  return (
    <div className='search-bar-container'>
      <input
        type="text"
        placeholder="Favourite games, genres, platform or even studio..."
        className="search-bar"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        onKeyDown={(e) => e.key === 'Enter' && handleSearch()} // Send request on Enter
      />
    </div>
  );
};

export default Search;
