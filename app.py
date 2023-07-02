import random


class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_player = None

    def display(self):
        print("  1 2 3 4 5 6 7")
        for row in self.board:
            print('|', end='')
            for cell in row:
                print(cell + '|', end='')
            print()
        print()

    def make_move(self, col):
        for row in range(5, -1, -1):
            if self.board[row][col] == ' ':
                self.board[row][col] = self.current_player
                return True
        return False

    def check_win(self):
        # Check rows
        for row in range(6):
            for col in range(4):
                if (self.board[row][col] == self.current_player and
                        self.board[row][col + 1] == self.current_player and
                        self.board[row][col + 2] == self.current_player and
                        self.board[row][col + 3] == self.current_player):
                    return True

        # Check columns
        for row in range(3):
            for col in range(7):
                if (self.board[row][col] == self.current_player and
                        self.board[row + 1][col] == self.current_player and
                        self.board[row + 2][col] == self.current_player and
                        self.board[row + 3][col] == self.current_player):
                    return True

        # Check diagonal (top left to bottom right)
        for row in range(3):
            for col in range(4):
                if (self.board[row][col] == self.current_player and
                        self.board[row + 1][col + 1] == self.current_player and
                        self.board[row + 2][col + 2] == self.current_player and
                        self.board[row + 3][col + 3] == self.current_player):
                    return True

        # Check diagonal (bottom left to top right)
        for row in range(3, 6):
            for col in range(4):
                if (self.board[row][col] == self.current_player and
                        self.board[row - 1][col + 1] == self.current_player and
                        self.board[row - 2][col + 2] == self.current_player and
                        self.board[row - 3][col + 3] == self.current_player):
                    return True

        return False


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        while True:
            col = input(f"{self.name}, enter your move (1-7): ")
            if col.isdigit() and 1 <= int(col) <= 7:
                col = int(col) - 1
                if board.make_move(col):
                    break
                else:
                    print("Column is full. Try again.")
            else:
                print("Invalid input. Try again.")


class AIPlayer(Player):
    def __init__(self, name, symbol):
        super().__init__(name, symbol)

    def make_move(self, board):
        while True:
            col = random.randint(0, 6)
            if board.make_move(col):
                break


def play_game():
    board = Board()

    print("Welcome to Connect 4!")
    print("Player 1, enter your name:")
    name1 = input()
    print("Player 2, enter your name:")
    name2 = input()

    player1 = Player(name1, 'X')
    player2 = None

    while True:
        print("\nChoose game mode:")
        print("1. Player vs Player")
        print("2. Player vs AI")
        mode = input()

        if mode == '1':
            player2 = Player(name2, 'O')
            break
        elif mode == '2':
            player2 = AIPlayer(name2, 'O')
            break
        else:
            print("Invalid input. Try again.")

    board.display()

    while True:
        board.current_player = player1.symbol
        player1.make_move(board)
        board.display()
        if board.check_win():
            print(f"{player1.name} wins!")
            break
        if all(cell != ' ' for row in board.board for cell in row):
            print("It's a draw!")
            break

        board.current_player = player2.symbol
        player2.make_move(board)
        board.display()
        if board.check_win():
            print(f"{player2.name} wins!")
            break
        if all(cell != ' ' for row in board.board for cell in row):
            print("It's a draw!")
            break


if __name__ == '__main__':
    play_game()
