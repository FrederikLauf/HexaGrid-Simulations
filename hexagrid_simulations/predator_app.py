# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:23:32 2020

@author: Frederik
"""

import hexagrid.app
import simulations.predator_simulation
import tkinter

# ------------------------------create main window-----------------------
if __name__ == '__main__':
    root = tkinter.Tk()
    new_predator_app = hexagrid.app.App(root, simulations.predator_simulation.PredatorSimulation())
    new_predator_app._window.title('Predator')
    root.mainloop()
