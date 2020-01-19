# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 14:41:54 2019

@author: Frederik
"""

import hexagrid.hexagrid
import hexagrid.agent
import random


            
class AntAgent(hexagrid.agent.Agent):
    
    def __init__(self,grid,position=[1,1],decision=None,name=None):
        
        super().__init__(grid,position,decision)
        self._name=name
    
    
    def _make_ant_decision(self,start=0,stop=5):
        """Randomly choose between surrounding cells with highest parameter 
        and return its direcition.""" 
        
        vicinity=self._make_scan(start,stop) # list with parameters of surrounding cells
        maximum=max(vicinity)
        
        if maximum == -1:
            return None
        
        options=[] # list with directions of cells sharing maximum
        for i in range(len(vicinity)):
            if vicinity[i]==maximum:
                options.append(self._grid._dictio[(i+start)%6])
        
        decision=options[random.randint(0,len(options)-1)] # random choice from options
        
        return decision
    
    def _leave_mark(self,value):
        
        self._grid._tab[self._position[0]][self._position[1]].set_param(value)


#-----------------------AntApp class-------------------------------------------------------        
class AntSimulation:
    
    def __init__(self):
        """Create AntApp instance."""
        
        
        
        self._World=hexagrid.hexagrid.HexaGrid(40,50)
        
        self._N=20
        
        self._Ant=[]
        for i in range(self._N):
            new_ant=AntAgent(self._World,[20+0*i,2],None,None)
            self._Ant.append(new_ant)
        
            
        
        self._active_ant=0
        
#        for i in range(1,8):
#            self._World._tab[2*i][i+10].set_param(-1)
#            self._World._tab[2*i+1][i+10].set_param(-1)
#            
#        for i in range(1,8):
#            self._World._tab[2*i][i+20].set_param(-1)
#            self._World._tab[2*i+1][i+20].set_param(-1)
            
        
        

    def _simulation_step(self):
    
        self._World._global_evaporate(1)
                
        decision=self._Ant[self._active_ant]._make_ant_decision(2,4)
        
        if random.randint(1,10) in range(1,3):
            decision=self._World._dictio[random.randint(2,4)]
            
        self._Ant[self._active_ant]._move(decision)
        self._Ant[self._active_ant]._leave_mark(500)
        
        if self._Ant[self._active_ant]._position[1]==self._World._width-1 and self._active_ant!=self._N-1:
            self._active_ant+=1
        
        
        
    def _display(self):
        """Returns a string visualising _World with _Ant on it."""
        
        ant_positions=[(self._Ant[l]._position[0],self._Ant[l]._position[1]) for l in range(self._N)]
        
        lines=''
        for j in range(self._World._height):   
             
            if j%2!=0:
                lines+='  '   
                 
            for k in range(self._World._width):
                
                if (j,k) in ant_positions:
                    lines+='X '
                elif self._World._tab[j][k].get_param()==-1:
                    lines+='# '
                elif self._World._tab[j][k].get_param()!=0:
                    lines+='o '                
                else:
                    lines+='  '
                        
            lines+='\n'
            
        return lines


    
    
        
        


                
