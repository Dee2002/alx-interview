#!/usr/bin/node

const request = require('request');

// Parse command-line arguments
const movieId = process.argv[2];

// Construct URL for Star Wars API endpoint
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Make HTTP GET request
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Unexpected status code:', response.statusCode);
  } else {
    // Parse JSON response
    const filmData = JSON.parse(body);

    // Extract list of characters
    const charactersUrls = filmData.characters;

    // Function to fetch character data asynchronously
    const fetchCharacterData = (url) => {
      return new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
          if (error) {
            reject(error);
          } else if (response.statusCode !== 200) {
            reject(`Unexpected status code: ${response.statusCode}`);
          } else {
            resolve(JSON.parse(body).name);
          }
        });
      });
    };

    // Fetch and print character data in order
    Promise.all(charactersUrls.map(fetchCharacterData))
      .then(characters => {
        characters.forEach(character => console.log(character));
      })
      .catch(error => console.error('Error:', error));
  }
});
