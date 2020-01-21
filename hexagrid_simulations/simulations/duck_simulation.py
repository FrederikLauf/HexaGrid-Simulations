# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 22:31:29 2020

@author: Frederik
"""

import hexagrid.hexagrid
import hexagrid.agent
import random



class DuckAgent(hexagrid.agent.Agent):
    
    def __init__(self,grid,position=[1,1],decision=None):
        
        super().__init__(grid,position,decision)
        
    def _make_mother_decision(self,start,stop):
        
        return self._grid._dictio[random.randint(start,stop)]
    
    
    def _make_chick_decision(self,d):
        
        
        vicinity=self._radial_scan(2)
        
        
        for i in range(len(vicinity[0])):
            if vicinity[0][i][0]==d:
                return None
        
        for i in range(len(vicinity[1])):
            
            for j in range(2):
                
                if vicinity[1][i][j]==d:
                    if j==0:
                        decision=self._grid._dictio[i]
                    if j==1:
                        decision= self._grid._dictio[i] if random.randint(0,1) else self._grid._dictio[i+1]
                    return decision
                
        return None
                    

    
    def _leave_mark(self,value):
        
        self._grid._tab[self._position[0]][self._position[1]].set_param(value)



class DuckSimulation:
    
    def __init__(self):
        
        self._max_steps=150
        self._step=0
        self._time_step=80
        
        self._World=hexagrid.hexagrid.HexaGrid(15,80)
        
        self._N=15
        
        self._Duck=[]
        for i in range(self._N):
            new_duck=DuckAgent(self._World,[7,self._N-i],None)
            self._Duck.append(new_duck)
            new_duck._leave_mark(i+1)
        
        
    
    def _simulation_step(self):
                
        decision=self._Duck[0]._make_mother_decision(2,4)
        self._Duck[0]._leave_mark(0)
        self._Duck[0]._move(decision)
        self._Duck[0]._leave_mark(1)
        
        for i in range(1,self._N):
            decision=self._Duck[i]._make_chick_decision(i)
            self._Duck[i]._leave_mark(0)
            self._Duck[i]._move(decision)
            self._Duck[i]._leave_mark(i+1)
            
        self._step+=1
            
            
    def _display(self):
        """Returns a string visualising _World with Ducks on it."""
        
        lines=''
        for j in range(self._World._height):   
             
            if j%2!=0:
                lines+='  '   
                 
            for k in range(self._World._width):
                
                if self._World._tab[j][k].get_param()==1:
                    lines+='Z '
                elif self._World._tab[j][k].get_param() in range(2,self._N+1):
                    lines+='2 '
                else:
                    lines+='  '
                    
            lines+='\n'
            
        return lines+str(self._step)