# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 17:40:03 2020

@author: Frederik
"""

import hexagrid.app
import simulations.duck_simulation
import tkinter

# ------------------------------create main window-----------------------
if __name__ == '__main__':
    root = tkinter.Tk()
    new_duck_app = hexagrid.app.App(root, simulations.duck_simulation.DuckSimulation())
    new_duck_app._window.title('Ducks')
    root.mainloop()
