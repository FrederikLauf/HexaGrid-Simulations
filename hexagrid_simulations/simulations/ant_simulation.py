# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 14:41:54 2019

@author: Frederik
"""

import hexagrid.hexagrid
import hexagrid.agent
import random


            
class AntAgent(hexagrid.agent.Agent):
    
    def __init__(self,grid,position=[1,1],decision=None,steps=0):
        
        super().__init__(grid,position,decision)
        self._steps=steps
    
    
    def _make_ant_decision(self,start=0,stop=5):
        """Randomly choose between surrounding cells with highest parameter 
        and return its direcition.""" 
        
        vicinity=self._make_scan(start,stop)
        maximum=max(vicinity)
        
        if maximum == -1:
            return None
        
        options=[] # list with directions of cells sharing maximum
        for i in range(len(vicinity)):
            if vicinity[i]==maximum:
                options.append(self._grid._dictio[(i+start)%6])
        
        decision=options[random.randint(0,len(options)-1)]
        
        return decision
    
    def _leave_mark(self,value):
        
        current_cell=self._grid._tab[self._position[0]][self._position[1]]
        
        current_value=current_cell.get_param()
        current_cell.set_param(value+current_value)


#-----------------------AntApp class-------------------------------------------------------        
class AntSimulation:
    
    def __init__(self):
        """Create AntSimulation instance."""
        
        self._max_steps=5000
        self._step=0
        self._time_step=15
        
        self._World=hexagrid.hexagrid.HexaGrid(40,50)
        
        self._target1=[(5+i,45) for i in range(7)]
        self._target2=[(25+i,45) for i in range(7)]
        
        for pos in self._target1:
            self._World._tab[pos[0]][pos[1]].set_param(-1)
            
        for pos in self._target2:
            self._World._tab[pos[0]][pos[1]].set_param(-1)
            
        
        self._N=80
        
        self._Ant=[]
        for i in range(self._N):
            new_ant=AntAgent(self._World,[20,2],None,0)
            self._Ant.append(new_ant)
        
            
        
        self._active_ant=[self._Ant.pop(0)]
        
        self._success_ant=[]
        


    def _simulation_step(self):
    
        self._World._global_evaporate(1)
        
        for ant in self._success_ant:
            
            decision=ant._make_ant_decision(5,7)
            ant._move(decision)
            ant._leave_mark(300)
            ant._steps+=1
            
            if ant._position[1]==2 and ant._position[0] in range(17,24):
                ant._steps=0
                self._success_ant.remove(ant)
                #self._Ant.append(ant)
                
            if ant._position[1]==0:
                self._success_ant.remove(ant)
        
        for ant in self._active_ant:
        
            decision=ant._make_ant_decision(2,4)
            
            if random.randint(1,100) in range(1,26) and decision!=None:
                decision=self._World._dictio[random.randint(2,4)]
            
            
            ant._move(decision)
            ant._leave_mark(150)
            ant._steps+=1
            
            if ant._steps==40 and self._Ant!=[]:                
                self._active_ant.append(self._Ant.pop())
                
            if (ant._position[1]==44 and 
                (ant._position[0] in range(5,12) 
                 or ant._position[0] in range(24,32))):                
                self._success_ant.append(ant)
                self._active_ant.remove(ant)
                
            if ant._position[1]==self._World._width-1:                
                self._active_ant.remove(ant)
        
                    
                    
        if self._active_ant==[] and self._Ant!=[]:
            self._active_ant.append(self._Ant.pop())            
            
        self._step+=1
        
        
        
    def _display(self):
        """Returns a string visualising _World with _Ant on it."""
        
        ant_positions=[(self._Ant[l]._position[0],
                        self._Ant[l]._position[1]) 
                       for l in range(len(self._Ant))]
        
        active_ant_positions=[(self._active_ant[l]._position[0],
                               self._active_ant[l]._position[1]) 
                              for l in range(len(self._active_ant))]
        
        success_ant_positions=[(self._success_ant[l]._position[0],
                                   self._success_ant[l]._position[1]) 
                                  for l in range(len(self._success_ant))]
        
        lines=''
        for j in range(self._World._height):   
             
            if j%2!=0:
                lines+='  '   
                 
            for k in range(self._World._width):
                
                if ((j,k) in ant_positions 
                        or (j,k) in active_ant_positions
                        or (j,k) in success_ant_positions):
                    
                    lines+='X '
                    
                elif self._World._tab[j][k].get_param()==-1:
                    
                    lines+='# '
                    
                elif self._World._tab[j][k].get_param()!=0:
                    
                    lines+='o '                
                    
                else:
                    
                    lines+='  '
                        
            lines+='\n'
            
        return lines+str(self._step)


    
    
        
        


                
