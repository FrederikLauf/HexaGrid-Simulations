# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 12:49:01 2020

@author: Frederik
"""

import hexagrid.hexagrid
import hexagrid.agent
import random
import winsound



class PredatorAgent(hexagrid.agent.Agent):
    
    def __init__(self,grid,position=[1,1],decision=None):
        
        super().__init__(grid,position,decision)

   
    def _localise_prey(self):
        
        for r in range(1,max(self._grid._width,self._grid._height)):
            
            scan=self._circ_scan(r)            
            start=random.randint(0,5)
            
            for i in range(start,start+6):
                
                if 1 in scan[i%6]:                    
                    
                    sector=i%6
                    start=random.randint(0,r-1)
                    
                    for j in range(start,start+r):
                        
                        if scan[sector][j%r]==1:
                            
                            pos=j%r                            
                            return (r,sector,pos)
        
        return False                    
                    
        
    def _make_predator_decision(self):
       
        prey_location=self._localise_prey()
        
        if prey_location==False:
            return None
        
        pos=prey_location[2]
        sector=prey_location[1]
        r=prey_location[0]
        
        if r%2==0:
            
            if pos < r/2:
                direction=self._grid._dictio[sector]
                
            elif pos == r/2:
                if random.randint(0,1):
                    direction=self._grid._dictio[sector]
                else:
                    direction=self._grid._dictio[(sector+1)%6]
                    
            else:
                direction=self._grid._dictio[(sector+1)%6]
                
        if r%2!=0:
            
            if pos <= (r+1)/2:
                direction=self._grid._dictio[sector]
            
            else:
                direction=self._grid._dictio[(sector+1)%6]
                
        return direction


class PreyAgent(hexagrid.agent.Agent):
    
    def __init__(self,grid,position=[1,1],decision=0):
        
        super().__init__(grid,position,decision=0)
        
    def _make_prey_decision(self):
        
        d=random.randint(self._decision-1,self._decision+1)
        new_decision=self._grid._dictio[d%6]
        self._decision=d%6
        
        destination=self._validate_course(new_decision,1)
        if destination==False or destination.get_param()!=0:
            d=random.randint(0,5)
            new_decision=self._grid._dictio[d]
            self._decision=d
        
            
        return new_decision
        
        
    

#------------------------------------------------------------------------------

class PredatorSimulation:
    
    def __init__(self):
        
        self._max_steps=450
        self._step=0
        self._time_step=75
        
        self._World=hexagrid.hexagrid.HexaGrid(40,60)
        
        self._prey_number=15
        
        self._Prey=[]
        for p in range(self._prey_number):
            i=random.randint(self._World._height//3,self._World._height-1)
            j=random.randint(self._World._width//3,self._World._width-1)
            new_prey=PreyAgent(self._World,[i,j],random.randint(0,5))
            self._Prey.append(new_prey)
            new_prey._leave_mark(1)
            
        self._Predator=PredatorAgent(self._World,[1,1],None)
        self._Predator._leave_mark(2)
        
        
    
    def _simulation_step(self):
        
        for prey in self._Prey:
            
            decision=prey._make_prey_decision()
            destination=prey._validate_course(decision,1)
            if destination!=False and destination.get_param()!=2:
                prey._leave_mark(0)
                prey._move(decision)
                prey._leave_mark(1)
        
        decision=self._Predator._make_predator_decision()
         
        self._Predator._leave_mark(0)
        self._Predator._move(decision)
        self._Predator._leave_mark(2)
            
        _Prey_copy=[self._Prey[i] for i in range(len(self._Prey))]       
        for p in _Prey_copy:
            
            if p._position==self._Predator._position:
                self._Prey.remove(p)


        self._step+=1
            
            
        

    def _display(self):
        
        lines=''
        for j in range(self._World._height):   
             
            if j%2!=0:
                lines+='  '   
                 
            for k in range(self._World._width):
                
                if self._World._tab[j][k].get_param()==1:
                    lines+='o '
                elif self._World._tab[j][k].get_param()==2:
                    lines+='X '
                else:
                    lines+='  '
                    
            lines+='\n'
            
            
        return lines+str(self._step)+','+str(len(self._Prey))