import numpy as np

def solution(park, routes):
    x = 0
    y = 0
    parkmap = []
    start = np.array([0, 0])
    
    directions = {
        "W": np.array([0, -1]),
        "E": np.array([0, 1]),
        "S": np.array([1, 0]),
        "N": np.array([-1, 0])
    }
    for row in park:
        parkmap.append(list(row)) 
        for j in row:
            if j == "S":
                start = np.array([x, y])
            y += 1
        x += 1
        y = 0
    
    now = start[:] 
    for move in routes:
        a, b = move.split()
        direction = a
        distance = int(b)
        
        new_position = now[:]  
        can_move = True
        
        for _ in range(distance):
            new_position = new_position + directions[direction]
            
            if 0 <= new_position[0] < len(parkmap) and 0 <= new_position[1] < len(parkmap[0]):
                if parkmap[new_position[0]][new_position[1]] == "X":
                    can_move = False
                    break
            else:
                can_move = False
                break
        
        if can_move:
            now = new_position[:]
    
    return [int(now[0]), int(now[1])] 
