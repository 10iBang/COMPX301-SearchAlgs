import fileinput
import sys
#Taukoriri Nooti 1322671
class Node:

    def __init__(self, position = None, parent = None):
        #parent of current node
        self.parent = parent
        self.position = position
        #total cost : f = g + h
        self.f = 0
        #Start node to current node cost
        self.g = 0
        #heuristic based estimated cost for current node to goal node
        self.h = 0
    
    #Object Equality 
    def __eq__(self, other):
        return self.position == other.position    
    #less-than comparison
    def __lt__(self, other):
         return self.f < other.f
        
def a_star(map, start, end, cost):
    
        #create vist and visited lists
        #The node we have yet to visit
        #states
        visit = []
        visited = []
        
        #create our start node = S and goal Node = G
        #initialise
        g_node = Node(end, None)
        g_node.g = g_node.h = g_node.f = 0
        s_node = Node(start, None)
        s_node.g = s_node.h = s_node.f = 0

        visit.append(s_node)
        length = len(visit)

        
        #loop until our visit list is empty

        while length > 0:

            visit.sort()
            
            #check current node if at goal
            curr_node = visit.pop(0)
           # print("another pop")
           # print(curr_node)
            #add our start node to visited list
            visited.append(curr_node)
            
            #check if have reach our destination
            if curr_node == g_node:
                path = []
                while curr_node != s_node:
                    #add current to our paths
                    path.append(curr_node.position)
                    curr_node = curr_node.parent
                #reverse path lowest to highest (x,y)
                return path[::-1]
                
            
            #get current node position x, yet
            node_pos = (curr_node.position[0], curr_node.position[1])
            
            #East, West, South, North. Directions we can move in
            directions = [(node_pos[0] + 1, node_pos[1]), (node_pos[0] - 1, node_pos[1]), (node_pos[0], node_pos[1] + 1), (node_pos[0], node_pos[1] - 1)]
            
            #loop through directions
            for d in directions:
                
                #get the next point according to our move/direction
                next_move = map.get(d)
               
                
                #check for land
                if(next_move == 'X'):
                    continue
                    
                #create new node for nearby position on the map
                nearest = Node(d, curr_node)
                
                #check if the nearest have been visited
                if(nearest in visited):
                    continue
                
                #nearest.g = curr_node + cost
                nearest.g = curr_node.g + cost
                #heuristic costs calculated from using euclidean distance
                nearest.h = (((nearest.position[0] - g_node.position[0]) ** 2) + ((nearest.position[1] - g_node.position[1]) ** 2))
                nearest.f = nearest.g + nearest.h
                #print("nearest", nearest.position[0])
                #check nearest is in visit list
                if(visit_append(visit, nearest) == True):
                    #add to visit list
                    visit.append(nearest)
     
        return "No path found"
   
#function check if nearest lowest cost is lower  
def visit_append(visit, nearest):
    for v in visit:
        if(nearest == v and nearest.f >= v.f ):
            return False
    return True


def main():
    try:
        map = {}
        start = None
        goal = None
        
        #drawing the map variables
        x_range = 0
        y_range = 0
        grid = []
        
        y = 0
        
        #reading the input from the file maps
        print("reading map...")
        print("")
        
        for line in fileinput.input():
            x = 0
            length = len(line)
            #test
            x_range = length
            for char in line:
            
            #Reading in cordinates of 
                asciichar = char
                grid.append(asciichar)
                map[(x, y)] = asciichar
                if (asciichar == 'S'):
                    start = (x, y)
                    #start_y = y
                if(asciichar == 'G'):
                    goal = (x, y)

                x += 1
            y += 1

            
        #print("maps:", map)

        
        movement_cost = 1
        
        best_path = a_star(map, start, goal, movement_cost)
        print("path:", best_path)
        print("")
        #sum movement cost
        print('Total Move to get to goal: {0}'.format(len(best_path)))  
        print("")

        #set our y range for the grid
        y_range = y   

        #each cell in the grid for the ascii map
        cell = 0

        #write ascii map to console
        #remove last item in the list for drawing purpose
        #so we keep the 'G' value in in the map instead of just 'S' ... '.'
        best_path = best_path[: -1]
        for col in range(y_range):
            #print("1")
            for row in range(x_range):
                tupp = (row, col)
                if tupp in best_path:
                    sys.stdout.write('.')

                    cell += 1
                else:    
                    sys.stdout.write(grid[cell])
                    cell += 1
       
    except Exception as e:
        print(e)
        exit
main()