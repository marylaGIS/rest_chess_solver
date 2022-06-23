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
