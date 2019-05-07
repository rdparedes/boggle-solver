import React from 'react';

const Letter = ({ text, row, col, onLetterChangeCallback }) => (
  <input
    type="text"
    className="letter"
    value={text}
    onChange={(e) => onLetterChangeCallback && onLetterChangeCallback(row, col, e.target.value)}
  />
);

const Board = ({ board, onLetterChangeCallback }) => (
  <div className="board">
    {board &&
      board.map((row, i) => (
        <div key={i}>
          {row.map((letter, j) => {
            return (
              <Letter
                key={`${letter}-${j}`}
                text={letter}
                row={i}
                col={j}
                onLetterChangeCallback={onLetterChangeCallback}
              />
            );
          })}
        </div>
      ))}
  </div>
);

export default Board;
