LETTERS = ["a", "b", "c", "d", "e", "f", "g", "h"]


def create_board():
    temp_board = []
    for field in range(8, 0, -1):
        row = []
        for letter in LETTERS:
            row.append(letter + str(field))
        temp_board.append(row)

    board = []
    for row in temp_board[::-1]:
        board.append(row)

    return board


board = create_board()


if __name__ == "__main__":
    for row in board:
        print(row)
