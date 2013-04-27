class TicTacToeBoard:
    def __init__(self):
        self.field = {"A1": ' ', "A2": ' ', "A3": ' ',
                      "B1": ' ', "B2": ' ', "B3": ' ',
                      "C1": ' ', "C2": ' ', "C3": ' '}

        self.board = '\n  -------------\n' +\
                     '3 | %s | %s | %s |\n' +\
                     '  -------------\n' +\
                     '2 | %s | %s | %s |\n' +\
                     '  -------------\n' +\
                     '1 | %s | %s | %s |\n' +\
                     '  -------------\n' +\
                     '    A   B   C  \n'

        self.winner = None
        self.turns = []
        self.last_turn = None

    def __str__(self):
        return self.board % (self.field["A3"], self.field["B3"],
                             self.field["C3"], self.field["A2"],
                             self.field["B2"], self.field["C2"],
                             self.field["A1"], self.field["B1"],
                             self.field["C1"])

    def __setitem__(self, spot, sign):

        if spot not in self.field:
            raise InvalidKey

        elif sign not in ['X', 'O']:
            raise InvalidValue

        elif self.field[spot] is not ' ':
            raise InvalidMove

        elif sign is self.last_turn:
            raise NotYourTurn

        else:
            self.field[spot] = sign
            self.turns.append(sign)
            self.last_turn = sign

    def __getitem__(self, spot):
        return self.field[spot]

    def game_status(self):
        if not self.winner:
            self.check()

        if not self.winner and len(self.turns) is not 9:
            return 'Game in progress.'

        elif not self.winner and len(self.turns) is 9:
            return 'Draw!'

        else:
            return '%s wins!' % self.winner

    def check_win(self, slot1, slot2, slot3):
        if self.field[slot1] == self.field[slot2] == self.field[slot3] != ' ':
            return True

    def check(self):
        winning = [["A1", "A2", "A3"], ["B1", "B2", "B3"],
                   ["C1", "C2", "C3"], ["A1", "B1", "C1"],
                   ["A2", "B2", "C2"], ["A3", "B3", "C3"],
                   ["A1", "B2", "C3"], ["A3", "B2", "C1"]]
        for row in winning:
            if self.check_win(row[0], row[1], row[2]):
                self.winner = self.field[row[0]]
                break


class TicTacToeError(Exception):
    pass


class InvalidMove(TicTacToeError):
    pass


class InvalidValue(TicTacToeError):
    pass


class InvalidKey(TicTacToeError):
    pass


class NotYourTurn(TicTacToeError):
    pass