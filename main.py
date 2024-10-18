


class TicTacToeGame:
    ROW_SIZE = 3
    COL_SIZE = 3

    def __init__(self, ai: bool = False):
        # Generate board using list comprehension, '-' represents empty space
        self.board = ['-' for _ in range(TicTacToeGame.ROW_SIZE * TicTacToeGame.COL_SIZE)]
        self.current_winner = None # Keep track of the winner
        self.game_over = False # Keep track of the game state
        self.ai = ai
        self.player_one = 'X' # Player 1 is X
        self.player_two = 'O' # Player 2 is O
        self.current_player = 0 # player 0 is X, player 1 is O

    def play(self):
        while not self.game_over:
            print("Player X first")
            self.draw_board()
            print("\n\nEnter the coordinates to make a move")
            x = int(input("Enter x: "))
            y = int(input("Enter y: "))
            self.make_move(x, y)
            current_winner, winning_state = self.validate_moves()
            if current_winner:
                print(f"Player {current_winner} wins in {winning_state}")

    def make_move(self, x: int, y: int):
        array_index = x * TicTacToeGame.COL_SIZE + y
        if self.board[array_index] == '-':
            self.board[array_index] = self.player_one if self.current_player == 0 else self.player_two
            self._change_turn()
            self.draw_board()
        else:
            print("Invalid move")

    def validate_moves(self):
        if "-" not in self.board:
            self.game_over = True

        for horizontal_line in range(3):
            if self.board[horizontal_line * TicTacToeGame.COL_SIZE] == self.board[horizontal_line * TicTacToeGame.COL_SIZE + 1] == self.board[horizontal_line * TicTacToeGame.COL_SIZE + 2] != '-':
                self.game_over = True
                self.current_winner = self.board[horizontal_line * TicTacToeGame.COL_SIZE]
                return (self.current_winner, f"horizontal line {horizontal_line}")

        for vertical_line in range(3):
            if self.board[vertical_line] == self.board[vertical_line + 3] == self.board[vertical_line + 6] != '-':
                self.game_over = True
                self.current_winner = self.board[vertical_line]
                return (self.current_winner, f"vertical line {vertical_line}")

        if self.board[0] == self.board[4] == self.board[8] != '-':
            self.game_over = True
            self.current_winner = self.board[0]
            return (self.current_winner, "diagonal line 1")

        if self.board[2] == self.board[4] == self.board[6] != '-':
            self.game_over = True
            self.current_winner = self.board[2]
            return (self.current_winner, "diagonal line 2")

        return (self.current_winner, None)

    def _change_turn(self):
        self.current_player = 1 if self.current_player == 0 else 0

    def draw_board(self):
        board_display = ""
        for board_col in range(3):
            column_data = self.board[board_col * TicTacToeGame.COL_SIZE: (board_col * TicTacToeGame.COL_SIZE) + TicTacToeGame.COL_SIZE]
            for col in range(TicTacToeGame.COL_SIZE):
                board_display += f"| {column_data[col]} "
            board_display += "|\n"
        print(board_display)

if __name__ == "__main__":
    game = TicTacToeGame()
    game.play()