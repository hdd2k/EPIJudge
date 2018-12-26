from test_framework import generic_test
from collections import namedtuple, deque



# -> Slow solution! NOT flipping as being iterated
def dfsSolution(x,y,image):
    Coord = namedtuple("Coord", ['x','y'])
    color = image[x][y]
    visited = set()
    def dfs(curr):
        if ((0 <= curr.x < len(image)) and (0 <= curr.y < len(image[0]))) and \
                (curr not in visited) and \
                (image[curr.x][curr.y] == color):
            visited.add(curr)
            offsets = [(1,0),(-1,0),(0,1),(0,-1)]
            for n in [Coord(curr.x + o[0], curr.y + o[1]) for o in offsets]:
                dfs(n)

    dfs(Coord(x,y))

    for c in visited:
        image[c.x][c.y] = (1 - image[c.x][c.y])

# -> Better optimized solution, BFS with deque to flip as iteration occurs
def bfsSolution(x,y,image):
    # No need for 'visited' set if considering colors before flip
    Coord = namedtuple("Coord", ['x','y'])
    color = image[x][y]

    cellsToFlip = deque([Coord(x,y)])
    while (len(cellsToFlip) > 0):
        curr = cellsToFlip.popleft()
        if (((0 <= curr.x < len(image)) and (0 <= curr.y < len(image[0]))) and \
                (image[curr.x][curr.y] == color)):
            image[curr.x][curr.y] = (1 - image[curr.x][curr.y])
            for o in [(1,0),(-1,0),(0,1),(0,-1)]:
                cellsToFlip.append(Coord(curr.x + o[0], curr.y + o[1]))

def flip_color(x, y, image):
    # TODO - you fill in here.
    # dfsSolution(x,y,image)
    bfsSolution(x,y,image)
    return


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_connected_regions.py",
                                       'painting.tsv', flip_color_wrapper))
