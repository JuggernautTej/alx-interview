#!/usr/bin/node

const request = require('request');

const id = process.argv[2];

if (!id) {
  console.error('Usage: ./0-starwars_characters.js <id>');
  process.exit(1);
}

const swapi = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request(swapi, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Status code ${response.statusCode}`);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  const charPromises = characters.map((charUrl) => {
    return new Promise((resolve, reject) => {
      request(charUrl, (charError, charResponse, charBody) => {
        if (charError) {
          reject(charError);
          return;
        }

        const character = JSON.parse(charBody);
        resolve(character.name);
      });
    });
  });
  Promise.all(charPromises)
    .then((cast) => {
      cast.forEach((character) => {
        console.log(character);
      });
    })
    .catch((error) => {
      console.error(error);
    });
});
