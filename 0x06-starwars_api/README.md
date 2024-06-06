# Star Wars Characters

## Description
This command-line script written in Node.js fetches and displays the characters of a Star Wars movie based on the provided movie ID using the Star Wars API.

## Installation
1. Clone this repository.
2. Ensure you have Node.js installed on your system.
3. Install the required dependencies by running:
    ```
    npm install request
    ```
4. Make the script executable by running:
    ```
    chmod +x 0-starwars_characters.js
    ```

## Usage
Run the script with the following command:

./0-starwars_characters.js <movieID>

sql

Replace `<movieID>` with the ID of the Star Wars movie you want to fetch characters for.

## Example
To fetch characters for "Return of the Jedi" (movie ID: 3), run:

./0-starwars_characters.js 3

markdown


## Requirements
- Node.js version 10.x
- `request` module
