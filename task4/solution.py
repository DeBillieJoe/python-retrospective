class TicTacToeBoard:
    STATUS_DRAW = 'Draw!'
    STATUS_WIN = 'wins!'
    STATUS_GAME_IN_PROGRESS = 'Game in progress.'
    _WINNING_ROWS = [["A1", "A2", "A3"], ["B1", "B2", "B3"],
                     ["C1", "C2", "C3"], ["A1", "B1", "C1"],
                     ["A2", "B2", "C2"], ["A3", "B3", "C3"],
                     ["A1", "B2", "C3"], ["A3", "B2", "C1"]]
    _KEYS = ["A3", "B3", "C3", "A2", "B2", "C2", "A1", "B1", "C1"]

    def __init__(self):
        self._field = {"A1": ' ', "A2": ' ', "A3": ' ',
                       "B1": ' ', "B2": ' ', "B3": ' ',
                       "C1": ' ', "C2": ' ', "C3": ' '}

        self.board = '\n  -------------\n' +\
                     '3 | {} | {} | {} |\n' +\
                     '  -------------\n' +\
                     '2 | {} | {} | {} |\n' +\
                     '  -------------\n' +\
                     '1 | {} | {} | {} |\n' +\
                     '  -------------\n' +\
                     '    A   B   C  \n'

        self._winner = None
        self._turns = 0
        self._last_turn = None

    def __str__(self):
        return self.board.format(*[self._field.get(key, " ")
                                   for key in self._KEYS])

    def __setitem__(self, spot, sign):

        if spot not in self._field:
            raise InvalidKey

        elif sign not in ['X', 'O']:
            raise InvalidValue

        elif self._field[spot] is not ' ':
            raise InvalidMove

        elif sign is self._last_turn:
            raise NotYourTurn

        else:
            self._field[spot] = sign
            self._turns += 1
            self._last_turn = sign

    def __getitem__(self, spot):
        return self._field[spot]

    def game_status(self):
        if not self._winner:
            self.__check()

        if not self._winner and self._turns is not 9:
            return self.STATUS_GAME_IN_PROGRESS

        elif not self._winner and self._turns is 9:
            return self.STATUS_DRAW

        else:
            return '{} {}'.format(self._winner, self.STATUS_WIN)

    def __check_win(self, *args):
        """
        Return if there is a winner in the
        row defined by `slot1`, `slot2`, `slot3`.
        """

        for sign in ["X", "O"]:
            if all(sign == self._field[slot] for slot in args):
                return True

    def __check(self):
        """Return if there is a winner in the game."""

        for row in self._WINNING_ROWS:
            if self.__check_win(row[0], row[1], row[2]):
                self._winner = self._field[row[0]]
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
