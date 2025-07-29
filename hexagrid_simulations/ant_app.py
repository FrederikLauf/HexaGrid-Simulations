# -*- coding: utf-8 -*-

import hexagrid.app
import simulations.ant_simulation
import tkinter

# ------------------------------create main window-----------------------------
if __name__ == '__main__':
    root = tkinter.Tk()
    new_ant_app = hexagrid.app.App(root, simulations.ant_simulation.AntSimulation())
    new_ant_app._window.title('Ants')
    root.mainloop()
