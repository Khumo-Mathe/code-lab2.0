import random

def generate_maze(width, height):
    maze = [["#" for _ in range(width)] for _ in range(height)]

    def carve_passages(x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 < nx < width and 0 < ny < height and maze[ny][nx] == "#":
                maze[ny - dy][nx - dx] = " "
                maze[ny][nx] = " "
                carve_passages(nx, ny)

    maze[1][1] = " "
    carve_passages(1, 1)
    return maze

def display_maze(maze):
    return "\n".join("".join(row) for row in maze)

# Example usage
maze = generate_maze(21, 15)
print(display_maze(maze))
