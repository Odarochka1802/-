import random
import time


class HumanPlayer:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        while True:
            try:
                row = int(input(f"{self.name}, введите номер строки (0-2): "))
                col = int(input(f"{self.name}, введите номер столбца (0-2): "))
                if board[row][col] == '-':
                    return (row, col)
                else:
                    print("Эта клетка уже занята. Попробуйте снова.")
            except ValueError:
                print("Неправильный ввод. Введите целые числа от 0 до 2.")


class RandomComputerPlayer:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == '-']
        return random.choice(empty_cells)


class TicTacToe:
    def __init__(self):
        self.board = [['-' for _ in range(3)] for _ in range(3)]  # Создаем игровое поле 3x3
        self.current_winner = None  # Переменная для хранения победителя

    def print_board_nums(self):
        nums_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in nums_board:
            print('| ' + ' | '.join(row) + ' |')

    def print_board(self):
        for row in self.board:
            print('| ' + ' | '.join(row) + ' |')

    def empty_squares(self):
        return any('-' in row for row in self.board)

    def make_move(self, square, letter):
        row, col = square
        if self.board[row][col] == '-':
            self.board[row][col] = letter
            return True
        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'  # Начинает игрок X

    while game.empty_squares():
        if letter == 'O':
            square = o_player.make_move(game.board)
        else:
            square = x_player.make_move(game.board)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' делает ход в клетку {square}')
                game.print_board()
                print('')  # Пустая строка для улучшения читаемости

            if game.current_winner:
                if print_game:
                    print(letter + ' побеждает!')
                return letter  # Конец игры

        letter = 'O' if letter == 'X' else 'X'  # Смена хода

    if print_game:
        print('Ничья!')


if __name__ == '__main__':
    x_player = HumanPlayer('Игрок X', 'X')
    o_player = RandomComputerPlayer('Компьютер O', 'O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
