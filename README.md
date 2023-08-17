# tictaccli

A simple command-line Tic-Tac-Toe game played against the computer.

![tictactoe-demo](https://github.com/erenoguzyesil/tictaccli/assets/65873434/055b8d6f-01a6-4597-9b0c-0a1c0fc3b571)

## Installation

```
pip install tictaccli
```

## Usage

Run the command after installing:
```
tictactoe
```

## Other things you can do

### `tictactoecli.mark.Mark` and `tictactoecli.board.Board` classes

The `Mark` class, which inherits the `Enum` class, has the following fields: `X, O, and NULL`

* `Mark.X` and `Mark.O` fields are self-explanatory; they are the two marks on a Tic-Tac-Toe board.
* `Mark.NULL` field represents an empty field in a Tic-Tac-Toe board.

The `Board` class acts as a Tic-Tac-Toe board, which holds its marks as `Mark` in the `positions` field of its instance.

Check out the code to see the other methods.

### `tictactoecli` module

The `tictactoecli` module contains a variety of functions related to the gameplay.

- `tictactoecli:play()` starts the Tic-Tac-Toe game, which can also be achieved by typing the `tictactoe` command in the Terminal after installation.
