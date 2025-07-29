# -*- coding: utf-8 -*-

from hexagrid.hexagrid import HexaGrid
from hexagrid.hexagrid import DIRECTIONS as DIR


# ------------------Agent moving in a grid-------------------------------------
class Agent:

    # --------------------Agent constructor------------------------------------
    def __init__(self, grid, position=[1, 1]):
        """
        Create Agent instance.

        :param grid: the grid on which the Agent lives
        :type grid: HexaGrid
        :param position: Associated Cartesian coordinates on the grid, defaults to [1,1]
        :type position: list of length two
        """
        self._position = position
        self._grid = grid

    def _show_agent(self):
        """Primitive output method for console."""
        for i in range(self._grid._height):
            line = ''
            if i % 2 != 0:
                line += ' '
            for j in range(self._grid._width):
                line += 'x ' if [i, j] == self._position else 'o '
            print(line)

    # -------------------------utility methods---------------------------------
    def _make_scan(self, start=0, stop=5):
        """
        Return a list with the parameters from the surrounding cells.
        Parameters of non-existent cells are formally -1.

        :param start: start direction for scan
        :type start: int
        :param stop: stop direction for scan
        :type stop: int
        """
        cell = self._grid._tab[self._position[0]][self._position[1]]
        scan = []
        for i in range(start, stop + 1):
            cell_of_interest = self._grid.make_direction(cell, DIR[i % 6])
            scan.append(cell_of_interest.get_param() if cell_of_interest else -1)
        return scan

    def _validate_course(self, direction, radius):
        """
        Return cell in direction in radius-distance or False,
        if non-existent.

        :param direction: direction of the targeted destination
        :type direction: str
        :param radius: distance to the targeted destination
        :type radius: int
        """
        current_cell = self._grid._tab[self._position[0]][self._position[1]]
        i = 0
        while current_cell and i < radius:
            current_cell = self._grid.make_direction(current_cell, direction)
            i += 1
        return current_cell

    def _circ_scan_interior(self, R):
        """
        Return array with parameters of all 6*R cells in distance R,
        or False, if at least one of these cells is inexistent.
        """
        scan = [[-1 for i in range(R)] for j in range(6)]
        current_cell = self._validate_course('W', R)
        for d in range(6):
            for l in range(R):
                if current_cell is False:
                    return False
                scan[d][l] = current_cell.get_param()
                direction = DIR[(d + 2) % 6]
                current_cell = self._grid.make_direction(current_cell, direction)
        return scan

    def _circ_scan_periph(self, R):
        """
        Return array with parameters of cells in distance R.
        Inexistent cells are formally given the value -1.
        This method uses an auxiliary grid and should be used only if required.
        """
        h = R if (self._position[0] - R) % 2 == 0 else R + 1
        aux_grid = HexaGrid(2 * h + 1, 2 * h + 1)
        current_cell = aux_grid._tab[h][0]
        scan = [[-1 for i in range(R)] for j in range(6)]
        for d in range(0, 6):
            direction = DIR[(d + 2) % 6]
            for l in range(R):
                i = current_cell._coord[0] + self._position[0] - h
                j = current_cell._coord[1] + self._position[1] - R
                if i in range(self._grid._height) and j in range(self._grid._width):
                    scan[d][l] = self._grid._tab[i][j].get_param()
                current_cell = aux_grid.make_direction(current_cell, direction)
        return scan

    def _circ_scan(self, R):
        """Performs _circ_scan_interior and if it fails, -_periph."""
        scan = self._circ_scan_interior(R)
        if scan is False:
            scan = self._circ_scan_periph(R)
        return scan

    def _radial_scan(self, radius):
        """Return a list of circular scans, corresponding to radii
        from 1 to radius. Return False if at least one cell is non-existent.
        """
        scan = []
        for i in range(1, radius + 1):
            circular_scan = self._circ_scan(i)
            scan.append(circular_scan)
        return scan

    def _move(self, decision):
        """
        Move to cell in the decided direction, if there is a cell.

        :type decision: str
        """
        if decision is not None:
            current_cell = self._grid._tab[self._position[0]][self._position[1]]
            new_cell = self._grid.make_direction(current_cell, decision)
            if new_cell:
                self._position = list(new_cell.get_coord())

    def _leave_mark(self, value):
        """
        Set the parameter of the current cell.

        :param value: the intended parameter value for the cell
        """
        self._grid._tab[self._position[0]][self._position[1]].set_param(value)


# --------------------------testing method-------------------------------------
def main():
    world = HexaGrid(10, 10)
    test_agent = Agent(world, [2, 5])
    print(test_agent._position)
    test_agent._show_agent()
    print(test_agent._circ_scan(3))


if __name__ == '__main__':
    main()
