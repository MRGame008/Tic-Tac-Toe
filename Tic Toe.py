class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'

    def print_board(self):
        for i in range(0, 9, 3):
            print('|'.join(self.board[i:i+3]))
            if i < 6:
                print('-----')

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def is_winner(self, player):
        # find win status rowly coly and diameterly
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]

        for condition in win_conditions:
            if all(self.board[i] == player for i in condition):
                return True
        return False

    def is_board_full(self):
        return ' ' not in self.board

    def game_over(self):
        return self.is_winner('X') or self.is_winner('O') or self.is_board_full()

    def evaluate_board(self):
        if self.is_winner('X'):
            return -1
        elif self.is_winner('O'):
            return 1
        else:
            return 0

    def minimax(self, depth, maximizing_player):
        if depth == 0 or self.game_over():
            return self.evaluate_board()

        if maximizing_player:
            max_eval = float('-inf')
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'O'
                    eval = self.minimax(depth - 1, False)
                    self.board[i] = ' '
                    max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'X'
                    eval = self.minimax(depth - 1, True)
                    self.board[i] = ' '
                    min_eval = min(min_eval, eval)
            return min_eval

    def find_best_move(self):
        best_val = float('-inf')
        best_move = -1

        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'
                move_val = self.minimax(2, False)
                self.board[i] = ' '

                if move_val > best_val:
                    best_move = i
                    best_val = move_val

        return best_move


def main():
    game = TicTacToe()

    while not game.game_over():
        game.print_board()
        if game.current_player == 'X':
            position = int(input("Enter your move (1-9): ")) - 1
            if not (0 <= position <= 8) or game.board[position] != ' ':
                print("Invalid move. Try again.")
                continue
        else:
            print("AI is thinking...")
            position = game.find_best_move()

        game.make_move(position)

    game.print_board()
    if game.is_winner('X'):
        print("You win!")
    elif game.is_winner('O'):
        print("AI wins!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    main()
