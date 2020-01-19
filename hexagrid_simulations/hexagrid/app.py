# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 14:41:54 2019

@author: Frederik
"""


import tkinter




      
class App:
    
    def __init__(self,window,simulation):
        """Create AntApp instance."""
        
        self._simulation=simulation
        
        self._counter=0
        
        self._window=window
        
        self._screen=tkinter.Label(self._window,text=self._simulation._display(),font='TkFixedFont')
        self._screen.pack()
        
        self._start_button=tkinter.Button(self._window,text="Los",command=self._play)
        self._start_button.pack()
        

        

        

            
    def _play(self):
        """Method invoked by the start button."""
                
        
        def _update_label():
            
            _max_steps=2000
            _time_step=40
            
            self._simulation._simulation_step()                
            self._screen.config(text=self._simulation._display(),font='TkFixedFont')
            self._counter+=1                        
            
            if self._counter<=_max_steps:
                self._screen.after(_time_step,_update_label)
                
        _update_label()
        

                

