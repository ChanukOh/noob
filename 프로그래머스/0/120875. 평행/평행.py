from itertools import combinations

def solution(dots):
    a = [0, 1, 2, 3]
    b = combinations(a, 2)
    
    for xy in b:
        xy1 = dots[xy[0]]
        xy2 = dots[xy[1]]
        
        slope1 = (xy2[1] - xy1[1]) / (xy2[0] - xy1[0])
        
        other_points = [dots[j] for j in a if j not in xy]
        slope2 = (other_points[1][1] - other_points[0][1]) / (other_points[1][0] - other_points[0][0])
        
        if slope1 == slope2:
            return 1
        
    return 0
