import random; 

class Conway():
	"""Conway's Game of Life implementation using Python rendered in P5 """
	def __init__(self, s=10,reps=100):
		self.grid = []; 
		self.size = s; 
		self.reps = reps;
		self.init_grid()

	# Initializes a random grid configuration or state (inital state)
	def init_grid(self):
		 
		for i in range(self.size):
			t = []; 
			for j in range(self.size):
				t.append(random.choice([0,1])); 
			self.grid.append(t); 
	
	# Prints grid in the terminal, for testing purposes
	def print_grid(self):
		for i in range(len(self.grid)):
			for j in range(len(self.grid)):
				print(self.grid[i][j], " ",end=""); 
			print(); 

	# Checks whether the positions are in the array or are they valid positons 
	def check_range(self,i,j):
	
		if (i >= len(self.grid)) or (j >= len(self.grid)) or (i < 0) or (j < 0):
			return False; 
		else:
			return True;  


	# Returns the amount of neigbours (live cells) surrounding a given cell in the grid 
	def get_neigbours(self, i, j):
		# left diagonal top
		nCount = 0
		if (self.check_range(i-1,j-1)):
			nCount += self.grid[i-1][j-1]; 
		# top 
		if (self.check_range(i-1,j)):
			nCount += self.grid[i-1][j];
		# right diagonal top 
		if (self.check_range(i-1,j+1)):
			nCount += self.grid[i-1][j+1]; 
		# left 
		if (self.check_range(i,j-1)):
			nCount += self.grid[i][j-1]; 
		# right
		if (self.check_range(i,j+1)):
			nCount += self.grid[i][j+1]; 
		# left diagonal bottom 
		if (self.check_range(i+1,j-1)):
			nCount += self.grid[i+1][j-1]; 
		# down 
		if (self.check_range(i+1,j)):
			nCount += self.grid[i+1][j]; 
		# right diagonal bottom 
		if (self.check_range(i+1,j+1)):
			nCount += self.grid[i+1][j+1]; 
		return nCount;

	# runs 1 timestep of the simulation and updates the grid of the new positions in the cell 
	def run_conway(self):	
		for i in range(len(self.grid)):
			for j in range(len(self.grid)):

					# Any cell living with fewer than two live neighbours dies, as if by underpopulation 
				if (self.grid[i][j] == 1 and self.get_neigbours(i,j) < 2):
					self.grid[i][j] = 0;				
					# Any live cell with two or 3 neigbours live and moves on to the next generation 
				if (self.grid[i][j] == 1 and (self.get_neigbours(i,j) == 2 or self.get_neigbours(i,j) == 3)):
					continue;
					# Any live cell with more than three live neigbours dies as if by overpopulation 
				if (self.grid[i][j] == 1 and self.get_neigbours(i,j) > 3):
					self.grid[i][j] = 0;
					# Any dead cell with exactly three live neigbours becomes a live cell as if by reproduction 
				if (self.grid[i][j] == 0 and self.get_neigbours(i,j) == 3):
					self.grid[i][j] = 1; 


		


# P5 implementation
from p5 import *; 
import time 

cells = 10;  
iterations = 100; 
square_size = 50;
delay_s = 0.2
c = Conway(s=cells, reps=iterations)
crep = 0

# Built in function of the Processing library, initalize window for displaying the simulation
def setup():
	size(cells*square_size,cells*square_size); 
	background(0); 
	crep = 0;

# Built in function of the Processing library, draws shapes on the screen. 
def draw():
	# Alive cells are yellow, dead cells are black 
	cGrid = c.grid; 
	xpos = 0;
	ypos = 0; 
	global crep; 
	crep += 1
	livecount=0
	deadcount=0
	no_stroke()
	for i in range(cells):
		for j in range(cells):
			if cGrid[i][j] == 1:
				livecount += 1
				fill(255,255,0);
			else:
				deadcount += 1
				fill(0,0,0);

			rect((xpos,ypos),square_size,square_size);
			xpos += square_size;

		ypos += square_size;
		xpos = 0;
	time.sleep(delay_s);
	#update conway
	c.run_conway();

	print("	Current iteration : {} Live Count : {} Dead Count : {}".format(crep,livecount,deadcount))
	
	if crep >= iterations:
		exit()

	
# Runs the simulation, another Built-In Function of the processing library 
run();




	

