import random

def generate_maze(width: int, height: int) -> list:
    maze = [[1 for _ in range(width)] for _ in range(height)]
    
    def carve(x, y):
        maze[y][x] = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = x + dx*2, y + dy*2
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 1:
                maze[y + dy][x + dx] = 0
                carve(nx, ny)
    
    carve(1, 1)
    return maze