# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 17:22:58 2019

@author: Frederik
"""


# --------------------hexagonal grid-----------------------------------------
class HexaGrid:

    # -------------nested cell class-----------------------------------------
    class _Cell:

        def __init__(self, parameter, coordinates):
            """Create _Cell instance.

            parameter      any object, typically a number
            coordinates    integer list with length two
            """

            self._param = parameter  # some property of the cell
            self._coord = coordinates  # associated cartesic coordinates

        # ---------------------public accessor and update methods-----------
        def get_param(self):
            return self._param

        def set_param(self, value):
            self._param = value

        def get_coord(self):
            return self._coord

    # ---------Hexagrid constructor------------------------------------------
    def __init__(self, height, width):
        """Create HexaGrid instance."""

        self._height = height
        self._width = width

        self._tab = [[self._Cell(0, [i, j]) for j in range(width)] for i in range(height)]

        self._dictio = {0: 'W', 1: 'NW', 2: 'NE', 3: 'E', 4: 'SE', 5: 'SW'}

    # -------------utility methods-------------------------------------------

    def make_direction(self, cell, direction):
        """Return cell in direction from current cell,
        or False if not possible.

        Odd rows are interpreted as being shifted half a unit to the right
        and the cartesic coordinates are determined from direction
        correspondingly.
        """

        i = cell._coord[0]  # abbrevation
        j = cell._coord[1]  # abbrevation

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

                if cell.get_param() != 0 and cell.get_param() != -1:
                    cell.set_param(cell.get_param()-step)

    def _show(self):
        """Primitive output method for console."""

        for i in range(self._height):
            line = ''
            if i % 2 != 0:
                line += ' '
            for j in range(self._width):
                line += 'o '
            print(line)
