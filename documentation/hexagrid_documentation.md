## hexagrid.py

### class HexaGrid

#### nested class
\_Cell

#### variables

\_height: number of rows
\_width: number of columns
\_tab: two-dimensional array (\_height times \_width) of \_Cell instances
\_dictio: equals `{0:'W',1:'NW',2:'NE',3:'E',4:'SE',5:'SW'}`

#### methods

##### \_\_init\_\_(height,width)
height: initialises \_height
width: initialises \_width

Initialises \_tab and \_dict.


##### make\_direction(cell,direction)
cell: instance of \_Cell
direction: direction in string form (cf. \_dictio)

Returns adjacent cell in direction from cell,  where odd rows of \_tab are interpreted as being shifted half a lattice size to the right, or False, if there is no such cell.

##### \_global\_evaporate(step=1)
step: a number

Reduces \_param of each cell by step.


##### \_show():
Prints the grid in the console.

### class \_Cell (nested in HexaGrid)

#### variables

\_param: a number
\_coord: associated cartesian coordinates in HexaGrid.\_tab as list of length two.

#### methods

##### \_\_init\_\_(parameter,coordinates)
parameter: initialise \_param
coordinates: initialise \_coord

##### get\_param()
Returns \_param.

##### set\_param()
Updates \_param.

##### get\_coord()
Returns \_coord.




## agent.py

### class Agent

#### variables
\_grid: the grid (type HexaGrid) on which the agent lives
\_position: associated cartesian coordinates in the grid
\_decision: a direction in string form (cf. HexaGrid.\_dictio)

#### methods

##### \_\_init\_\_(grid,position=[1,1],decision=None)
grid: initialises \_grid
position: initialises \_position
decision: initialises \_decision


##### \_make\_scan(start=0,stop=5)
start, stop: directions in integer form (cf. HexaGrid.\_dictio)

Returns a list of length stop-start+1 with \_param of all adjacent cells in the 
directions from start to stop.

##### \_validate\_course(direction,radius)
direction: direction in string form (cf. HexaGrid.\_dictio)
radius: an integer

Returns the cell in radius distance in direction, or False, if there is no cell.

##### \_circ\_scan\_interior(R)
R: an integer

Return array with parameters of all 6\*R cells in distance R, 
or False, if at least one of these cells is inexistent. 
The array is a list of length six, whose elements are lists of length R.
Each contains the parameters of the cells on a hexagon side, starting at
a corner and going in clockwise direction until before the next corner.
The starting corner is in the west direction.

##### \_circ\_scan\_periph(R)
R: an integer

Return array with parameters of all 6\*R cells in distance R.
Parameters of inexistent cells are formally -1. The array is structured as
described for \_circ\_scan\_interior.

##### \_circ\_scan(R)
R: an integer

Returns  \_circ\_scan\_interior or, if it would be False,  \_circ\_scan\_periph.

##### \_radial scan(radius)
radius: an integer

Returns a list of \_circ\_scan for radii one to radius.
##### \_move(direction)
direction: direction in string form (cf. HexaGrid.\_dictio)

Changes \_position to the coordinates \_coord of the cell in direction.
##### \_show\_agent()
Prints the agent on its grid in the console.

## app.py

### class App

#### variables
\_simulation: Instance of simulations.[...]\_simulation.[...]Simulation
\_counter: an integer for counting simulation steps
\_window: tkinter root window
\_screen: tkinter label serving as display
\_start\_button: tkinter button serving as start button

#### methods

##### \_\_init\_\_(window,simulation)
window: initialises \_window
simulation: initialises \_simulation

Initialises window elements.

##### \_play()
Method invoked by start button, which runs and displays a simulation corresponding to \_simulation.

