# A very fair voting machine

## Description
This Python module provides an implementation of various voting algorithms to decide on a winning movie based on people's preferences. The module is designed to be extensible, allowing for the addition of new voting algorithms as needed. Each algorithm implemented in the module follows a standard interface and has unique methods for determining the winner based on the rankings provided by the voters.

## Features
- Extensible architecture for adding new voting algorithms.
- Abstract base class `VotingAlgorithm` to ensure consistency in algorithm implementation.
- Sample implementations of different voting strategies.
- A main function that randomly selects a voting algorithm to determine the winning movie.

## Usage
To use this module, create a list of votes where each vote is a list of movie rankings. Each movie is represented by a unique identifier (such as an integer). Pass this list of votes to the `main()` function to see which movie wins according to a randomly selected voting algorithm.

Example:
```python
votes = [
    [1, 3, 4, 2, 5],
    [2, 3, 4, 5, 1],
    [2, 4, 3, 1, 5],
    [1, 3, 4, 2, 5]
]

main(votes)
```

## Requirements
- Python 3.x
- Standard Python Libraries: `abc`, `collections`, `random`

## Contributing
Contributions to this project are welcome. Please follow standard best practices for code style and commit messages. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT License](https://opensource.org/licenses/MIT)
