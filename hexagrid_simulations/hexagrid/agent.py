# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 17:22:58 2019

@author: Frederik
"""

import hexagrid.hexagrid


# ----------------Agent moving in a grid--------------------------------------
class Agent:

    # ------------------Agent constructor-------------------------------------
    def __init__(self, grid, position=[1, 1], decision=None):
        """Create Agent instance.

        grid        a grid (assumed a HexaGrid instance),
                    on which the Agent lives
        position    cartesian coordinates associated with position on the grid
        decision    a direction, in which the Agent intends to move
        """

        self._position = position
        self._decision = decision
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

    # -----------------------utility methods----------------------------------
    def _make_scan(self, start=0, stop=5):
        """Return a list with the parameters from the surrounding cells.
        Parameters of non-existent cells are formally -1.
        """

        cell = self._grid._tab[self._position[0]][self._position[1]]
        dictio = self._grid._dictio

        scan = []
        for i in range(start, stop+1):
            cell_of_interest = self._grid.make_direction(cell, dictio[i % 6])
            if cell_of_interest:
                scan.append(cell_of_interest.get_param())
            else:
                scan.append(-1)

        return scan

    def _validate_course(self, direction, radius):
        """Return cell in direction in radius-distance or False,
        if non-existent.
        """

        current_cell = self._grid._tab[self._position[0]][self._position[1]]
        i = 0

        while current_cell and i < radius:
            current_cell = self._grid.make_direction(current_cell, direction)
            i += 1

        return current_cell

    def _circ_scan_interior(self, R):
        """Return array with parameters of all 6*R cells in distance R,
        or False, if at least one of these cells is inexistent."""

        scan = [[-1 for i in range(R)] for j in range(6)]
        current_cell = self._validate_course('W', R)

        for d in range(6):
            for l in range(R):
                if current_cell is False:
                    return False
                scan[d][l] = current_cell.get_param()
                direction = self._grid._dictio[(d+2) % 6]
                current_cell = self._grid.make_direction(current_cell, direction)

        return scan

    def _circ_scan_periph(self, R):
        """Return array with parameters of cells in distance R.
        Inexistent cells are formally given the value -1.
        This method uses an auxiliary grid and should be used only if required.
        """

        h = R if (self._position[0] - R) % 2 == 0 else R + 1
        aux_grid = hexagrid.hexagrid.HexaGrid(2 * h + 1, 2 * h + 1)
        current_cell = aux_grid._tab[h][0]
        scan = [[-1 for i in range(R)] for j in range(6)]

        for d in range(0, 6):
            direction = self._grid._dictio[(d + 2) % 6]
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
        if scan is not False:
            scan = self._circ_scan_periph(R)

        return scan

    def _radial_scan(self, radius):
        """Return a list of circular scans, corresponding to radii
        from 1 to radius. Return False if at least one cell is non-existent.
        """

        scan = []
        for i in range(1, radius+1):
            circular_scan = self._circ_scan(i)
            scan.append(circular_scan)

        return scan

    def _move(self, decision):
        """Move to cell in the decided direction, if there is a cell."""

        if decision is not None:
            current_cell = self._grid._tab[self._position[0]][self._position[1]]
            new_cell = self._grid.make_direction(current_cell, decision)
            if new_cell:
                self._position[0] = new_cell._coord[0]
                self._position[1] = new_cell._coord[1]

    def _leave_mark(self, value):

        self._grid._tab[self._position[0]][self._position[1]].set_param(value)


# ------------------------testing method--------------------------------------
def main():
    World = hexagrid.HexaGrid(10, 10)
    TestAgent = Agent(World, [2, 5], None)
    print(TestAgent._position)
    TestAgent._show_agent()
    print(TestAgent._circ_scan(3))


if __name__ == '__main__':
    main()
