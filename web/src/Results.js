import React from 'react';

class Word extends React.PureComponent {
  render() {
    const { value } = this.props.word;
    return <span>{value}</span>;
  }
}

const Results = ({ results }) => (
  <div className="results">
    <h3>Results</h3>
    <div className="results-container">
      {results && results.words.map(word => <Word word={word} />)}
    </div>
  </div>
);

export default Results;
