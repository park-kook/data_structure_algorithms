from collections import deque

# Sample grid
grid = [
    ['x', 'x', 'x', '_', '_'],
    ['_', 'x', 'y', 'y', '_'],
    ['_', 'y', 'y', '_', '_'],
    ['x', 'x', '_', '_', '_']
]

# Helper function simulating Pinterest's API
def isSameObject(p1, p2):
    r1, c1 = p1
    r2, c2 = p2

    # If either pixel is empty, return False
    if grid[r1][c1] == '_' or grid[r2][c2] == '_':
        return False

    # Return True if both characters are the same (same object)
    return grid[r1][c1] == grid[r2][c2]

# BFS-based object counting algorithm
def countObjects(grid, isSameObject):
    rows, cols = len(grid), len(grid[0])
    visited = set()  # tracks visited pixels
    objects = 0      # final object count

    # Helper: get valid 4-direction neighbors
    def get_neighbors(r, c):
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                yield (nr, nc)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '_' or (r, c) in visited:
                continue  # skip empty or visited

            # New object found
            objects += 1
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))

            while queue:
                cur = queue.popleft()
                for nei in get_neighbors(*cur):
                    if nei in visited:
                        continue
                    if grid[nei[0]][nei[1]] == '_':
                        continue
                    # Only add if part of same object
                    if isSameObject(cur, nei):
                        visited.add(nei)
                        queue.append(nei)

    return objects

# Run it
print("Number of objects in the grid:", countObjects(grid, isSameObject))







'''
given an array of visits(user_id, location_id, start_time, end_time) 
and an array of users infected with covid19 users write a function 
that returns the total number fusers that caught covid-19. 
when a user gets infected they will start infecting other users 
afterwards immediately meaning the person becomes contagious 
right after being infected and there is no incubation period. 
infected = [1], infection_simulator(visits, infected). 
visits =[[0,0,1,3],[0,1,4,5],[0,2,8,9],1,1,4,6],[2,2,7,9],[3,2,6,8]]
'''

visits = [
    [0, 0, 1, 3],
    [0, 1, 4, 5],
    [0, 2, 8, 9],
    [1, 1, 4, 6],  # initial infected
    [2, 2, 7, 9],
    [3, 2, 6, 8]
]
infected = [1]
from collections import defaultdict, deque

def infection_simulator(visits, initially_infected):
    # Step 1: Organize visits by location
    location_visits = defaultdict(list)
    user_visits = defaultdict(list)  # user_id -> list of (location, start, end)

    for user_id, loc_id, start, end in visits:
        location_visits[loc_id].append((user_id, start, end))
        user_visits[user_id].append((loc_id, start, end))

    # Step 2: Sort visits at each location
    for loc in location_visits:
        location_visits[loc].sort(key=lambda x: x[1])

    # Step 3: Track infection time
    infection_time = dict()
    for uid in initially_infected:
        infection_time[uid] = float('-inf')  # infected from the beginning

    # Step 4: BFS infection propagation
    queue = deque(initially_infected)

    while queue:
        contagious_user = queue.popleft()
        contagious_from = infection_time[contagious_user]

        for loc_id, c_start, c_end in user_visits[contagious_user]:
            # Only visits after infection are contagious
            if c_end <= contagious_from:
                continue  # this visit happened before infection

            visits_at_loc = location_visits[loc_id]
            for other_user, o_start, o_end in visits_at_loc:
                if other_user == contagious_user:
                    continue
                if other_user in infection_time:
                    continue  # already infected

                # Check for overlapping time
                overlap_start = max(c_start, o_start)
                overlap_end = min(c_end, o_end)

                if overlap_start < overlap_end:
                    # Infection can happen only if contagious user is infected during overlap
                    if overlap_end > contagious_from:
                        infection_time[other_user] = overlap_start
                        queue.append(other_user)

    return len(infection_time)
