# Problem description

Create a web-based solver for Boggle. Users should be able to enter their boggle "board" into the webapp and retrieve a list of matching words.

# Rules

- 16 letter cubes
- 4 x 4 grid
- Goal: have the highest point total
- To gain points: create words from randomly assorted letters in the cube grid.
  - The longer the word, the higher the point value of it.webapp
  - Words should be created using adjoining letters - horizontally, vertically, or diagonally.
  - Words can be spelled in any direction, including backwards
  - Can't use a letter cube multiple times on the same word.
  - Any word found in a standard English dictionary is permissible, except nouns (people or places)
- Multiple meanings of the same word do not earn multiple points
- Variations of spelling for a word are counted as individual words
- Plural and singular words are separate, and should both be written and scored if they can be created.

### Scoring

| No. of letters | Points per word |
| -------------- | --------------- |
| 3              | 1               |
| 4              | 1               |
| 5              | 2               |
| 6              | 3               |
| 7              | 5               |
| 8+             | 11              |

# Credits

- Dictionary obtained from https://github.com/machineboy2045/fast-boggle-solver
