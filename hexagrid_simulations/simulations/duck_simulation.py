# -*- coding: utf-8 -*-

from hexagrid.hexagrid import HexaGrid
from hexagrid.hexagrid import DIRECTIONS as DIR
from hexagrid.agent import Agent
from random import randint


class DuckAgent(Agent):

    def __init__(self, grid, position=[1, 1]):

        super().__init__(grid, position)

    @staticmethod
    def _make_mother_decision(start, stop):
        return DIR[randint(start, stop)]

    def _make_chick_decision(self, d):

        vicinity = self._radial_scan(2)

        for i in range(len(vicinity[0])):
            if vicinity[0][i][0] == d:
                return None

        for i, v in enumerate(vicinity[1]):
            for j in range(2):
                if v[j] == d:
                    if j == 0:
                        decision = DIR[i]
                    else:
                        decision = DIR[i] if randint(0, 1) else DIR[i + 1]
                    return decision
        return None

    def _leave_mark(self, value):

        self._grid._tab[self._position[0]][self._position[1]].set_param(value)


class DuckSimulation:

    def __init__(self):

        self._max_steps = 150
        self._step = 0
        self._time_step = 80

        self._World = HexaGrid(15, 80)

        self._N = 15

        self._Duck = []
        for i in range(self._N):
            new_duck = DuckAgent(self._World, [7, self._N - i])
            self._Duck.append(new_duck)
            new_duck._leave_mark(i + 1)

    def _simulation_step(self):

        decision = self._Duck[0]._make_mother_decision(2, 4)
        self._Duck[0]._leave_mark(0)
        self._Duck[0]._move(decision)
        self._Duck[0]._leave_mark(1)

        for i in range(1, self._N):
            decision = self._Duck[i]._make_chick_decision(i)
            self._Duck[i]._leave_mark(0)
            self._Duck[i]._move(decision)
            self._Duck[i]._leave_mark(i + 1)

        self._step += 1

    def _display(self):
        """Returns a string visualising _World with Ducks on it."""
        lines = ''
        for j in range(self._World._height):
            if j % 2 != 0:
                lines += '  '
            for k in range(self._World._width):
                if self._World._tab[j][k].get_param() == 1:
                    lines += 'Z '
                elif self._World._tab[j][k].get_param() in range(2, self._N + 1):
                    lines += '2 '
                else:
                    lines += '  '
            lines += '\n'

        return lines + str(self._step)
