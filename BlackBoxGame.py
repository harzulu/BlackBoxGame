# Author: Benjamin McFarland
# Date: August 7th, 2020
# Description: The Black Box board game. Originally by Eric Solomon


class BlackBoxGame:

    def __init__(self, atom_list):
        """
        initializes all of the variables
        """
        self._player_score = 25
        self._atoms_left = 4
        self._board = [['-' for i in range(10)] for j in range(10)]
        for atom in atom_list:
            self._board[atom[1]][atom[0]] = 1

    def print_board(self):
        """
        prints the current board with all the information
        """
        for row in self._board:
            for column in row:
                print(column, end=" ")
            print()

    def shoot_ray(self, column, row):
        """
        Takes in the row/column of the ray shot, adjusts the player's score,
        then returns the coordinates of the exit square the ray exits by calling functions to check board.
        If the origin square does not exist it returns false. And if the guess ray is a hit it returns None.
        """
        if row == 0:
            if column == 0:
                return False
            elif column == 9:
                return False
            else:
                self._player_score -= 1
                output = self.ray_down(row, column)
                if output is None:
                    self._board[row][column] = 'H'
                    return output
                else:
                    self._player_score -= 1
                    self._board[row][column] = 'I'
                    self._board[output[0]][output[1]] = 'O'
                    return output

        elif row == 9:
            if column == 0:
                return False
            elif column == 9:
                return False
            else:
                self._player_score -= 1
                output = self.ray_up(row, column)
                if output is None:
                    self._board[row][column] = 'H'
                    return output
                else:
                    self._player_score -= 1
                    self._board[row][column] = 'I'
                    self._board[output[0]][output[1]] = 'O'
                    return output

        elif column == 0:
            if row == 0:
                return False
            elif row == 9:
                return False
            else:
                self._player_score -= 1
                output = self.ray_right(row, column)
                if output is None:
                    self._board[row][column] = 'H'
                    return output
                else:
                    self._player_score -= 1
                    self._board[row][column] = 'I'
                    self._board[output[0]][output[1]] = 'O'
                    return output

        elif column == 9:
            if row == 0:
                return False
            elif row == 9:
                return False
            else:
                self._player_score -= 1
                output = self.ray_left(row, column)
                if output is None:
                    self._board[row][column] = 'H'
                    return output
                else:
                    self._player_score -= 1
                    self._board[row][column] = 'I'
                    self._board[output[0]][output[1]] = 'O'
                    return output
        else:
            return False

    def ray_up(self, row, column):
        """
        Checks to see if there are any atoms nearby to cause a move.
        If at the edge of board, returns tuple of that row and column
        If a hit, returns False
        If an atom is diagonal moves in opposite direction of atom by calling function for that direction.
        If nothing continues in up-ward direction
        """
        if row - 1 == 0:
            end_tuple = (column, row - 1)
            return end_tuple
        elif self._board[row - 1][column] == 1:
            return None
        elif self._board[row - 1][column + 1] == 1:
            if self._board[row - 1][column - 1] == 1:
                return self.ray_down(row, column)
            return self.ray_left(row, column)
        elif self._board[row - 1][column - 1] == 1:
            if self._board[row - 1][column + 1] == 1:
                return self.ray_down(row, column)
            return self.ray_right(row, column)
        else:
            return self.ray_up(row - 1, column)

    def ray_down(self, row, column):
        """
        Checks to see if there are any atoms nearby to cause a move.
        If at the edge of board, returns tuple of that row and column
        If a hit, returns False
        If an atom is diagonal moves in opposite direction of atom by calling function for that direction.
        If nothing continues in down-ward direction
        """
        if row + 1 == 9:
            end_tuple = (column, row + 1)
            return end_tuple
        elif self._board[row + 1][column] == 1:
            return None
        elif self._board[row + 1][column + 1] == 1:
            if self._board[row + 1][column - 1] == 1:
                return self.ray_up(row, column)
            return self.ray_left(row, column)
        elif self._board[row + 1][column - 1] == 1:
            if self._board[row + 1][column + 1] == 1:
                return self.ray_up(row, column)
            return self.ray_right(row, column)
        else:
            return self.ray_down(row + 1, column)

    def ray_left(self, row, column):
        """
        Checks to see if there are any atoms nearby to cause a move.
        If at the edge of board, returns tuple of that row and column
        If a hit, returns False
        If an atom is diagonal moves in opposite direction of atom by calling function for that direction.
        If nothing continues in left direction
        """
        if column - 1 == 0:
            end_tuple = (column - 1, row)
            return end_tuple
        elif self._board[row][column - 1] == 1:
            return None
        elif self._board[row - 1][column - 1] == 1:
            if self._board[row + 1][column - 1] == 1:
                return self.ray_right(row, column)
            return self.ray_down(row, column)
        elif self._board[row + 1][column - 1] == 1:
            if self._board[row - 1][column - 1] == 1:
                return self.ray_right(row, column)
            return self.ray_up(row, column)
        else:
            return self.ray_left(row, column - 1)

    def ray_right(self, row, column):
        """
        Checks to see if there are any atoms nearby to cause a move.
        If at the edge of board, returns tuple of that row and column
        If a hit, returns False
        If an atom is diagonal moves in opposite direction of atom by calling function for that direction.
        If nothing continues in right direction
        """
        if column + 1 == 9:
            end_tuple = (column + 1, row)
            return end_tuple
        elif self._board[row][column + 1] == 1:
            return None
        elif self._board[row - 1][column + 1] == 1:
            if self._board[row + 1][column + 1] == 1:
                return self.ray_left(row, column)
            return self.ray_down(row, column)
        elif self._board[row + 1][column + 1] == 1:
            if self._board[row - 1][column + 1] == 1:
                return self.ray_left(row, column)
            return self.ray_up(row, column)
        else:
            return self.ray_right(row, column + 1)

    def guess_atom(self, row, column):
        """
        Takes in the row/column of the guessed atom location. If there is an atom there, returns True.
        If there is no atom there, returns False. Adjusts player's score accordingly
        Calls the print_board method at start and end of this method
        """
        if self._board[column][row] == 1:
            return True
        else:
            return False

    def get_score(self):
        """
        Returns the player's current score
        """
        return self._player_score

    def atoms_left(self):
        """
        Returns the number of atoms on the board that haven't been guessed yet
        """
        return self._atoms_left