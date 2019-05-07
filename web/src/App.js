import React from 'react';
import Board from './Board.js';
import Results from './Results.js';
import './App.css';

class App extends React.PureComponent {
  state = {
    board: [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']],
    results: null,
    isLoading: false
  };

  randomizeBoard = () => {
    const { board } = this.state;
    const updatedBoard = board.map(row =>
      row.map(_ => String.fromCharCode(97 + Math.floor(Math.random() * 26)))
    );
    this.setState({
      board: updatedBoard
    });
  };

  solveBoard = async () => {
    const { board } = this.state;
    this.setState({ isLoading: true });
    const res = await fetch('/find-words', {
      method: 'POST',
      body: JSON.stringify({
        board: board
      }),
      headers: {
        'Content-Type': 'application/json'
      }
    });
    const data = (await res.json()).data;
    this.setState({ isLoading: false });

    this.updateResults(data);
  };

  updateResults = results => {
    this.setState({ results });
  };

  onLetterChange = (row, col, value) => {
    const { board } = this.state;
    board[row][col] = value;
    this.setState({ board });
    this.forceUpdate();
  };

  render() {
    const { board, results, isLoading } = this.state;
    return (
      <div className="App">
        <h1>Boggle Solver</h1>
        <div className="row">
          <Board flex="1" board={board} onLetterChangeCallback={this.onLetterChange} />
          <Results flex="1" results={results} />
        </div>
        <button onClick={this.solveBoard} disabled={isLoading && 'disabled'}>
          {isLoading ? 'Loading...' : 'Solve'}
        </button>
        <button onClick={this.randomizeBoard}>Randomize</button>
      </div>
    );
  }
}

export default App;
