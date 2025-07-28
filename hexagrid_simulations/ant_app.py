# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 17:40:03 2020

@author: Frederik
"""
import hexagrid.app
import simulations.ant_simulation
import tkinter

# ------------------------------create main window-----------------------------
if __name__ == '__main__':
    root = tkinter.Tk()
    new_ant_app = hexagrid.app.App(root, simulations.ant_simulation.AntSimulation())
    new_ant_app._window.title('Ants')
    root.mainloop()
