# -*- coding: utf-8 -*-

from hexagrid.hexagrid import HexaGrid
from hexagrid.hexagrid import DIRECTIONS as DIR
from hexagrid.hexagrid import DIRECTIONS_INVERSE as DIR_INV
from hexagrid.agent import Agent
import random


class PredatorAgent(Agent):

    def __init__(self, grid, position=[1, 1]):

        super().__init__(grid, position)

    def _localise_prey(self):

        for r in range(1, max(self._grid._width, self._grid._height)):
            scan = self._circ_scan(r)
            start = random.randint(0, 5)
            for i in range(start, start + 6):
                if 1 in scan[i % 6]:
                    sector = i % 6
                    start = random.randint(0, r - 1)
                    for j in range(start, start + r):
                        if scan[sector][j % r] == 1:
                            pos = j % r
                            return r, sector, pos
        return False

    def _make_predator_decision(self):

        prey_location = self._localise_prey()
        if prey_location is False:
            return None
        r, sector, pos = prey_location

        if r % 2 == 0:
            if pos < r / 2:
                direction = DIR[sector]
            elif pos == r / 2:
                if random.randint(0, 1):
                    direction = DIR[sector]
                else:
                    direction = DIR[(sector + 1) % 6]
            else:
                direction = DIR[(sector + 1) % 6]
        else:
            if pos <= (r + 1) / 2:
                direction = DIR[sector]
            else:
                direction = DIR[(sector + 1) % 6]

        return direction


class PreyAgent(Agent):

    def __init__(self, grid, position=[1, 1]):

        super().__init__(grid, position)
        self._decision = random.randint(0, 5)
        self._awareness_radius = 5
        
    def _localise_prey(self):

        for r in range(1, self._awareness_radius + 1):
            scan = self._circ_scan(r)
            start = random.randint(0, 5)
            for i in range(start, start + 6):
                if 1 in scan[i % 6]:
                    sector = i % 6
                    start = random.randint(0, r - 1)
                    for j in range(start, start + r):
                        if scan[sector][j % r] == 1:
                            pos = j % r
                            return r, sector, pos
        return False

    def _localise_predator(self):

        for r in range(1, self._awareness_radius + 1):
            scan = self._circ_scan(r)
            start = random.randint(0, 5)
            for i in range(start, start + 6):
                if 2 in scan[i % 6]:
                    sector = i % 6
                    start = random.randint(0, r - 1)
                    for j in range(start, start + r):
                        if scan[sector][j % r] == 2:
                            pos = j % r
                            return r, sector, pos
        return False

    def _make_prey_decision(self):

        # Check for predator
        predator_location = self._localise_predator()
        if predator_location is not False:
            r, sector, pos = predator_location
            if r % 2 == 0:
                if pos < r / 2:
                    direction = DIR[sector]
                elif pos == r / 2:
                    if random.randint(0, 1):
                        direction = DIR[sector]
                    else:
                        direction = DIR[(sector + 1) % 6]
                else:
                    direction = DIR[(sector + 1) % 6]
            else:
                if pos <= (r + 1) / 2:
                    direction = DIR[sector]
                else:
                    direction = DIR[(sector + 1) % 6]
            dir_inv = DIR_INV[direction]
            direction = DIR[(dir_inv + 3) % 6]
            self._decision = DIR_INV[direction]
            # d = random.randint(self._decision - 1, self._decision + 1)
            # direction = DIR[d % 6]
            # self._decision = d % 6
            return direction

        # check for prey friend
        prey_location = self._localise_prey()
        if prey_location is not False:
            r, sector, pos = prey_location
            if r % 2 == 0:
                if pos < r / 2:
                    direction = DIR[sector]
                elif pos == r / 2:
                    if random.randint(0, 1):
                        direction = DIR[sector]
                    else:
                        direction = DIR[(sector + 1) % 6]
                else:
                    direction = DIR[(sector + 1) % 6]
            else:
                if pos <= (r + 1) / 2:
                    direction = DIR[sector]
                else:
                    direction = DIR[(sector + 1) % 6]
            self._decision = DIR_INV[direction]
            d = random.randint(self._decision - 1, self._decision + 1)
            direction = DIR[d % 6]
            self._decision = d % 6
            return direction

        # Random decision
        d = random.randint(self._decision - 1, self._decision + 1)
        direction = DIR[d % 6]
        self._decision = d % 6

        destination = self._validate_course(direction, 1)
        if destination is False or destination.get_param() != 0:
            d = random.randint(0, 5)
            direction = DIR[d]
            self._decision = d

        return direction


# ------------------------------------------------------------------------------

class PredatorFishSimulation:

    def __init__(self):

        self._max_steps = 2000
        self._step = 0
        self._time_step = 25

        self._World = HexaGrid(40, 60)

        self._Prey = []
        for i in range(12):
            for j in range(12):
                new_prey = PreyAgent(self._World, [20 + i, 20 + j])
                self._Prey.append(new_prey)
                new_prey._leave_mark(1)
        self._prey_number = len(self._Prey)

        self._Predator = PredatorAgent(self._World, [1, 1])
        self._Predator._leave_mark(2)
        
        self._Predator2 = PredatorAgent(self._World, [1, 5])
        self._Predator2._leave_mark(2)

    def _simulation_step(self):

        for prey in self._Prey:
            decision = prey._make_prey_decision()
            destination = prey._validate_course(decision, 1)
            if destination is not False and destination._param == 0:
                prey._leave_mark(0)
                prey._move(decision)
                prey._leave_mark(1)

        decision = self._Predator._make_predator_decision()
        destination = self._Predator._validate_course(decision, 1)
        if destination is not False and destination._param != 2:
            self._Predator._leave_mark(0)
            self._Predator._move(decision)
            self._Predator._leave_mark(2)
        
        decision = self._Predator2._make_predator_decision()
        destination = self._Predator2._validate_course(decision, 1)
        if destination is not False and destination._param != 2:
            self._Predator2._leave_mark(0)
            self._Predator2._move(decision)
            self._Predator2._leave_mark(2)

        for p in self._Prey[:]:
            if p._position == self._Predator._position or p._position == self._Predator2._position:
                self._Prey.remove(p)

        self._step += 1

    def _display(self):

        lines = ''
        for j in range(self._World._height):
            if j % 2 != 0:
                lines += '  '
            for k in range(self._World._width):
                if self._World._tab[j][k].get_param() == 1:
                    lines += 'o '
                elif self._World._tab[j][k].get_param() == 2:
                    lines += 'X '
                else:
                    lines += '  '
            lines += '\n'

        return lines + str(self._step) + ',' + str(len(self._Prey))
