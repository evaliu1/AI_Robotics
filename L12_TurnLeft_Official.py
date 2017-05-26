# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D below.
# Official Program

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

def optimum_policy2D(grid,init,goal,cost):
    value = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))]]

    closed = [[[' ' for row in range(len(grid[0]))] for col in range(len(grid))],
              [[' ' for row in range(len(grid[0]))] for col in range(len(grid))],
              [[' ' for row in range(len(grid[0]))] for col in range(len(grid))],
              [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]]

    
     plan = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

    change = True
    while change:
        change = False
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                for c in range(4):
                    if goal[0]==x and goal[1]==y:
                        if value[c][x][y]>0:
                            change = True
                            value[c][x][y]=0
                            closed[c][x][y]='*'
                    elif grid[x][y]==0:
                        for i in range(3):
                            c2 = (c+action[i])%4
                            x2 = x + forward[c2][0]
                            y2 = y + forward[c2][1]

                            if x2>=0 and x2<len(grid) and y2>=0 and y2<len(grid[0]) and grid[x2][y2]==0:
                                v2 = value[c2][x2][y2] + cost[i]
                                if v2< value[c][x][y]:
                                    value[c][x][y]=v2
                                    closed[c][x][y]=action_name[i]
                                    change = True
    x = init[0]
    y = init[1]
    c = init[2]

    plan[x][y] = closed[c][x][y]
    while closed[c][x][y] != '*':
        if closed[c][x][y] == '#':
            c2 = c
        elif closed[c][x][y] == 'R':
            c2 = (c-1)%4
        elif closed[c][x][y] == 'L':
            c2 = (c+1)%4
        x = x + forward[c2][0]
        y = y + forward[c2][1]
        c = c2
        plan[x][y] = closed[c][x][y]

    for i in range(len(plan)):
        print plan

    return plan

optimum_policy2D(grid,init,goal,cost)
                                



    
