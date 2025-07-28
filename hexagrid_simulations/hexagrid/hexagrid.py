# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 17:22:58 2019

@author: Frederik
"""

DIRECTIONS = {0: 'W', 1: 'NW', 2: 'NE', 3: 'E', 4: 'SE', 5: 'SW'}


# -----------------------hexagonal grid----------------------------------------
class HexaGrid:
    # ----------------nested cell class----------------------------------------
    class _Cell:

        def __init__(self, coordinates, parameter):
            """
            Create a _Cell instance.

            :param coordinates: associated Cartesian coordinates
            :type coordinates: tuple of length two
            :param parameter: some property of the cell
            """
            self._coord = coordinates
            self._param = parameter

        # ---------------------public accessor and update methods--------------
        def get_param(self):
            return self._param

        def set_param(self, value):
            self._param = value

        def get_coord(self):
            return self._coord

    # ------------HexaGrid constructor-----------------------------------------
    def __init__(self, height, width):
        """
        Create HexaGrid instance.
        """
        self._height = height
        self._width = width
        self._tab = [[self._Cell((i, j), 0) for j in range(width)] for i in range(height)]
        self._dictio = {0: 'W', 1: 'NW', 2: 'NE', 3: 'E', 4: 'SE', 5: 'SW'}

    # ----------------utility methods------------------------------------------

    def make_direction(self, cell, direction):
        """
        Return cell in direction from current cell,
        or False if not possible.

        :param cell: The cell from which to take the direction.
        :type cell: _Cell
        :param direction: The direction in which the returned cell lies.
        :type direction: string
        :returns: The cell in the given direction of the given cell.
        :rtype: _Cell
        """
        i, j = cell.get_coord()
        # column shift
        if i % 2 == 0:  # i is even
            if 'W' in direction:
                if j != 0:
                    j -= 1
                else:
                    return False
            if 'E' == direction:
                if j != self._width - 1:
                    j += 1
                else:
                    return False
        else:  # i is odd
            if 'E' in direction:
                if j != self._width - 1:
                    j += 1
                else:
                    return False
            if 'W' == direction:
                if j != 0:
                    j -= 1
                else:
                    return False
        # row shift
        if 'N' in direction:
            if i != 0:
                i -= 1
            else:
                return False
        if 'S' in direction:
            if i != self._height - 1:
                i += 1
            else:
                return False

        return self._tab[i][j]

    def _global_evaporate(self, step=1):

        for i in range(self._height):
            for j in range(self._width):
                cell = self._tab[i][j]
                param = cell.get_param()
                if param not in {0, -1}:
                    new_param = param - step if param > step else 0
                    cell.set_param(new_param)

    def _show(self):
        """Primitive output method for console."""
        for i in range(self._height):
            line = ''
            if i % 2 != 0:
                line += ' '
            for j in range(self._width):
                line += 'o '
            print(line)


if __name__ == "__main__":
    hg = HexaGrid(5, 5)
    print(hg._height)
    hg._show()
    help(HexaGrid)
