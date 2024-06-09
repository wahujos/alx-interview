#!/usr/bin/node
// files we will require

const request = require('request');

// Function to fetch characters of a specific movie
function fetchCharacters (movieId) {
  return new Promise((resolve, reject) => {
    const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
    request(filmUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`Failed to fetch film: ${response.statusCode}`));
      } else {
        const film = JSON.parse(body);
        const characterUrls = film.characters;
        const charactersPromises = characterUrls.map(url => fetchCharacterName(url));
        Promise.all(charactersPromises)
          .then(characters => resolve(characters))
          .catch(error => reject(error));
      }
    });
  });
}

// Function to fetch character name from character URL
function fetchCharacterName (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`Failed to fetch character: ${response.statusCode}`));
      } else {
        const character = JSON.parse(body);
        resolve(character.name);
      }
    });
  });
}

// Main function
function main () {
  const movieId = process.argv[2]; // Get movie ID from command line argument
  if (!movieId) {
    console.error('Please provide a movie ID as a command line argument.');
    process.exit(1);
  }

  fetchCharacters(movieId)
    .then(characters => {
      characters.forEach(character => console.log(character));
    })
    .catch(error => console.error('Error:', error));
}

// Run the main function
main();
