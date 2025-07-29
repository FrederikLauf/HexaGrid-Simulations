# -*- coding: utf-8 -*-

import hexagrid.app
import simulations.predator_fish_simulation
import tkinter

# ------------------------------create main window-----------------------
if __name__ == '__main__':
    root = tkinter.Tk()
    new_predator_fish_app = hexagrid.app.App(root, simulations.predator_fish_simulation.PredatorFishSimulation())
    new_predator_fish_app._window.title('Predator fish')
    root.mainloop()
