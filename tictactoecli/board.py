from tictactoecli.mark import Mark
import re

class Board:
    """
    This class represents a Tic-Tac-Toe board, which holds its marks in the `positions` field of an instance.
    """
    def __init__(self):
        """
        Initiates a new Tic-Tac-Toe board and `positions` and `winning_positions` fields.
        
        - `positions` is a 2-dimensional list of marks separated by rows.
        - `winning_positions` is a list of `[row, column]` positions, where if each row-column position in an inner list corresponds to the same mark, it results in the win of the player of it.

        ```
        board = Board()

        board.winning_positions
        # ^ returns:
        # Rows
        [ [ [0, 0], [0, 1], [0, 2] ], 
          [ [1, 0], [1, 1], [1, 2] ],
          [ [2, 0], [2, 1], [2, 2] ], 
              
        # Columns
          [ [0, 0], [1, 0], [2, 0] ], 
          [ [0, 1], [1, 1], [2, 1] ],
          [ [0, 2], [1, 2], [2, 2] ],
          
        # Diagonals
          [ [0, 0], [1, 1], [2, 2] ],
          [ [2, 0], [1, 1], [0, 2] ]
        ]
        ```
        """
        self.positions = [[Mark.NULL] * 3 for _ in range(3)]
        # row | col: 0          1           2
        # 0:  [ [Mark.NULL, Mark.NULL, Mark.NULL] ],
        # 1:  [ [Mark.NULL, Mark.NULL, Mark.NULL] ],
        # 2:  [ [Mark.NULL, Mark.NULL, Mark.NULL] ]

        self.winning_positions = []  # [ [[0, 0], [0, 1], [0, 2]], ... ]

        for row_index in range(3):
            self.winning_positions.append([])
            for col_index in range(3):
                self.winning_positions[row_index].append(
                    [row_index, col_index])

        for col_index in range(3, 6):
            self.winning_positions.append([])
            for row_index in range(3):
                self.winning_positions[col_index].append(
                    [row_index, col_index - 3])

        self.winning_positions.append([[0, 0], [1, 1], [2, 2]])
        self.winning_positions.append([[2, 0], [1, 1], [0, 2]])

    def place_mark(self, row_pos: int, col_pos: int, mark: Mark):
        """
        Sets a member of `Mark` in `positions` in the given `row_pos` (row index, max. 2) and `col_pos` (column index, max. 2) only if `row_pos` and `col_pos` indexes of `positions` are Mark.NULL (empty)
        """
        if [row_pos, col_pos] in self.available_positions():
            self.positions[row_pos][col_pos] = mark

    def get_mark(self, row_pos: int, col_pos: int) -> Mark:
        """
        Returns the `Mark` in `row_pos` (row index, max. 2) and `col_pos` (column index, max. 2) of `positions`
        """
        return self.positions[row_pos][col_pos]

    def check_win(self) -> Mark:
        """
        Checks whether the game has a winner and returns the winner's mark. If there is no winner or it is tie, then returns `Mark.NULL`
        """
        for positions_list in self.winning_positions:
            marks_scanned = []

            for position in positions_list:
                marks_scanned.append(self.get_mark(*position))

            if len(set(marks_scanned)) == 1:
                # check if `marks_scanned` contains only X's, O's, or NULL's

                return marks_scanned[0]

            marks_scanned.clear()

        return Mark.NULL  # when no winner is detected

    def is_tie(self):
        """
        Returns `True` if the there are no empty positions and winner, otherwise `False`
        """
        return len(self.available_positions()) == 0 and self.check_win() is Mark.NULL

    def available_positions(self):
        """
        Returns a list of [row, column] positions where `positions[row][col]` returns `Mark.NULL` (empty)
        """
        result = []

        for row in range(3):
            for col in range(3):
                if self.positions[row][col] is Mark.NULL:
                    result.append([row, col])

        return result

    def positions_to_win(self, mark: Mark):
        """
        Returns an array of [row, column] positions that can result in the instant win of the player of `mark`

        Example:
        ```
        board.positions = 
            [ [X,    X, NULL] ],
            [ [X,    O, NULL] ],
            [ [NULL, O, O] ]

        board.positions_to_win(Mark.X) #=> [ [0, 2], [2, 0] ]
        ```
        """
        result = []

        for positions_list in self.winning_positions:
            marks_scanned = []
            empty_spots = []

            for position in positions_list:
                if self.get_mark(*position) is mark:
                    marks_scanned.append(position)
                else:
                    empty_spots.append(position)

                if len(marks_scanned) == 2 and len(empty_spots) != 0 and (empty_spots[0]) in self.available_positions():
                    result.append(empty_spots[0])

            marks_scanned.clear()
            empty_spots.clear()

        return result
    

    def __str__(self):
        string = """
       |       |   
   1   |   2   |   3   
       |       |
———————————————————————
       |       |   
   4   |   5   |   6   
       |       |
———————————————————————
       |       |   
   7   |   8   |   9   
       |       |
"""

        # Making the `self.positions` list one-dimensional, flattening the list
        positions_1d = [mark for row in self.positions for mark in row]

        for i in range(9):
            if positions_1d[i] == Mark.X:
                string = re.sub(re.escape(str(
                    i + 1)) + '(?!.*\\033\[[a-zA-Z0-9_];*[a-zA-Z0-9_]*m)', '\033[1;91mX\033[0m', string)

            if positions_1d[i] == Mark.O:
                string = re.sub(re.escape(str(
                    i + 1)) + '(?!.*\\033\[[a-zA-Z0-9_];*[a-zA-Z0-9_]*m)', '\033[1;94mO\033[0m', string)

        return string
