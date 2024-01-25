# Создаем игровое поле
board = [' ' for _ in range(9)]

# Функция для отображения игрового поля
def display_board():
    for i in range(3):
        row = '|'.join(board[i*3:(i+1)*3])
        print(row)
        if i < 2:
            print('-' * 5)

# Функция для хода игрока
def make_move(player, position):
    board[position] = player

# Функция для проверки победителя
def check_winner(player):
    # Проверяем горизонтали, вертикали и диагонали
    return ((board[0] == board[1] == board[2] == player) or
            (board[3] == board[4] == board[5] == player) or
            (board[6] == board[7] == board[8] == player) or
            (board[0] == board[3] == board[6] == player) or
            (board[1] == board[4] == board[7] == player) or
            (board[2] == board[5] == board[8] == player) or
            (board[0] == board[4] == board[8] == player) or
            (board[2] == board[4] == board[6] == player))

# Основной игровой цикл
def main():
    display_board()
    player = 'X'

    while True:
        position = int(input(f'Player {player}, введите номер ячейки (0-8): '))
        if position < 0 or position > 8 or board[position] != ' ':
            print('Некорректный ход, попробуйте снова.')
            continue
        make_move(player, position)
        display_board()
        if check_winner(player):
            print(f'Игрок {player} победил!')
            break
        if ' ' not in board:
            print('Ничья!')
            break
        player = 'O' if player == 'X' else 'X'

main()
