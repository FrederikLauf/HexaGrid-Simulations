# -*- coding: utf-8 -*-

import hexagrid.app
import simulations.predator_simulation
import tkinter

# ------------------------------create main window-----------------------
if __name__ == '__main__':
    root = tkinter.Tk()
    new_predator_app = hexagrid.app.App(root, simulations.predator_simulation.PredatorSimulation())
    new_predator_app._window.title('Predator')
    root.mainloop()
