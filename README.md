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

The `Board` class acts as a Tic-Tac-Toe board, which holds its marks in the `positions` field of an instance.

* `Board().positions` is the list of marks of a table. It is a two-dimensional list separated by rows.
* `Board().winning_positions` is a list of `[row, column]` positions, where if each row-column position in an inner list corresponds to the same mark, it results in the win of the player of it.
* `Board().place_mark(row_pos: int, col_pos: int, mark: Mark)` method allows you to place a mark on the empty positions of a Tic-Tac-Toe board.
* `Board().get_mark(row_pos: int, col_pos: int)` method returns the `Mark` element in `Board().positions` list.
