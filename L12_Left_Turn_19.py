# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's 
# optimal path to the position specified in goal; 
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a 
# right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 20] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid,init,goal,cost):
    value = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))]
            [[999 for row in range(len(grid[0]))] for col in range(len(grid))]
            [[999 for row in range(len(grid[0]))] for col in range(len(grid))]
            [[999 for row in range(len(grid[0]))] for col in range(len(grid))]]
    value[][2][0] = 0

    closed = [[[0 for row in range(len(grid[0]))] for col in range(len(grid))]
            [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
            [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
            [[0 for row in range(len(grid[0]))] for col in range(len(grid))]]
    closed[][2][0] = 1

    
    plan = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand
    count = 0

    x = init[0]
    y = init[1]
    z = init[2]
    g = 0

    open = [[g, x, y, z]]
    
    while not found and not resign:
        if len(open) == 0:
            resign = True
            return "Fail"
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            z = next[3]
            g = next[0]
            
            for x in range(len(grid)):
                for y in range(len(grid[0])):
                    #When the direction is up = 0
                    if c==0:
                        if goal[0] == x and goal[1] == y:
                            if value[c][x][y] > 0:
                                value[c][x][y] = 0
                                plan[x][y] = '*'
                                change = True
                          
                        elif grid[x][y] == 0:
                            for i in range(len(forward)):
                                x2 = x + forward[i][0]
                                y2 = y + forward[i][1]
                                if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                                    # Turn right condition
                                    if ((grid[x][y-1]== 1)and(grid[x+1][y]==0)) or ((y-1<0)and(grid[x+1][y]==0)):
                                        z2 = (z - 1)%4
                                        v2 = value[c][x2][y2] + cost[0]
                                        g2 = g + cost[0]
                                        plan[x2][y2] = 'R'
                                    # Turn left condition 
                                    elif ((grid[x][y-1]==1)and(grid[x-1][y]==0)) or ((y-1<0)and(grid[x-1][y]==0)):
                                        z2 = (z + 1)%4
                                        v2 = value[c][x2][y2] + cost[2]
                                        g2 = g + cost[2]
                                        plan[x2][y2] = 'L'
                                    # No turn condition
                                    else:
                                        z2 = z
                                        g2 = g + cost[1]
                                        v2 = value[c][x2][y2] + cost[1]
                                        plan[x2][y2] = '#'
                                    
                                    # Not sure about the following codes!!!!!!!!!!!!!!!!!!!!!!!!!!
                                    if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                                        g2 = g + cost
                                        open.append([g2, x2, y2, z2])
                                        closed[x2][y2] = 1

                                        

    for i in range(len(plan)):
        print plan[i]
    
    return plan
