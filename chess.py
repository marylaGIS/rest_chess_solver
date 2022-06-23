FILES = ["a", "b", "c", "d", "e", "f", "g", "h"]
RANKS = [1, 2, 3, 4, 5, 6, 7, 8]


class Figure:
    def __init__(self, file, rank):
        self.file = file  # a-h
        self.rank = rank  # 1-8

    def list_available_moves(self):
        pass

    def validate_move(self):
        pass


class King(Figure):
    def list_available_moves(self):
        available_moves_list = []

        if self.file == 'a' and self.rank == 1:
            available_moves_list.append(('a' + str(self.rank + 1)))
            available_moves_list.append(('b' + str(self.rank)))
            available_moves_list.append(('b' + str(self.rank + 1)))
        if self.file in FILES[1:7] and self.rank == 1:
            for file in FILES[1:7]:
                available_moves_list.append(file + str(self.rank))

        if self.rank not in RANKS or self.file not in FILES:
            available_moves_list = ['Field does not exist']

        return list(set(available_moves_list))
