from src.maze_generator import generate_maze

def test_maze_dimensions():
    maze = generate_maze(10, 10)
    assert len(maze) == 10
    assert all(len(row) == 10 for row in maze)

def test_maze_has_paths():
    maze = generate_maze(15, 15)
    assert sum(cell for row in maze for cell in row) < 225  # No todo son paredes