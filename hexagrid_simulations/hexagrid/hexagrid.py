# -*- coding: utf-8 -*-


DIRECTIONS = {0: 'W', 1: 'NW', 2: 'NE', 3: 'E', 4: 'SE', 5: 'SW'}
DIRECTIONS_INVERSE = {'W': 0, 'NW': 1, 'NE': 2, 'E': 3, 'SE': 4, 'SW': 5}


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
        i, j = cell._coord
        match direction:
            case 'W':
                j -= 1
            case 'NW':
                if i % 2 == 0:
                    j -= 1
                i -= 1
            case 'SW':
                if i % 2 == 0:
                    j -= 1
                i += 1
            case 'E':
                j += 1
            case 'NE':
                if i % 2 != 0:
                    j += 1
                i -= 1
            case 'SE':
                if i % 2 != 0:
                    j += 1
                i +=1
        if i < 0 or i > self._height - 1 or j < 0 or j > self._width - 1:
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
