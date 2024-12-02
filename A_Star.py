from pyMaze import maze, agent, COLOR, textLabel
from queue import PriorityQueue


def heuristic(cell_a, cell_b):
    x1, y1 = cell_a
    x2, y2 = cell_b
    return abs(x1 - x2) + abs(y1 - y2)


def astar_solver(maze_obj, start=None):
    if start is None:
        start = (maze_obj.rows, maze_obj.cols)

    priority_queue = PriorityQueue()
    priority_queue.put((heuristic(start, maze_obj._goal), start))

    explored_path = {}
    visited_nodes = [start]

    g_cost = {cell: float("inf") for cell in maze_obj.grid}
    g_cost[start] = 0

    f_cost = {cell: float("inf") for cell in maze_obj.grid}
    f_cost[start] = heuristic(start, maze_obj._goal)

    while not priority_queue.empty():
        current = priority_queue.get()[1]
        visited_nodes.append(current)

        if current == maze_obj._goal:
            break

        for direction in "ESNW":
            if maze_obj.maze_map[current][direction]:
                if direction == 'E':
                    neighbor = (current[0], current[1] + 1)
                elif direction == 'W':
                    neighbor = (current[0], current[1] - 1)
                elif direction == 'N':
                    neighbor = (current[0] - 1, current[1])
                elif direction == 'S':
                    neighbor = (current[0] + 1, current[1])

                tentative_g_cost = g_cost[current] + 1
                tentative_f_cost = tentative_g_cost + heuristic(neighbor, maze_obj._goal)

                if tentative_f_cost < f_cost[neighbor]:
                    explored_path[neighbor] = current
                    g_cost[neighbor] = tentative_g_cost
                    f_cost[neighbor] = tentative_f_cost
                    priority_queue.put((f_cost[neighbor], neighbor))

    solution_path = {}
    step = maze_obj._goal
    while step != start:
        solution_path[explored_path[step]] = step
        step = explored_path[step]

    return visited_nodes, explored_path, solution_path



def display_results(maze_obj, search_path, backtrack_path, solution_path):
    search_agent = agent(maze_obj, footprints=True, color=COLOR.blue, filled=True)
    backtrack_agent = agent(maze_obj, 1, 1, footprints=True, color=COLOR.yellow, filled=True, goal=(maze_obj.rows, maze_obj.cols))
    solution_agent = agent(maze_obj, footprints=True, color=COLOR.red)

    maze_obj.tracePath({search_agent: search_path}, delay=300)
    maze_obj.tracePath({backtrack_agent: backtrack_path}, delay=300)
    maze_obj.tracePath({solution_agent: solution_path}, delay=300)

    textLabel(maze_obj, 'A* Path Length', len(solution_path) + 1)
    textLabel(maze_obj, 'A* Search Length', len(search_path))


def main():
    maze_obj = maze(10, 10)
    maze_obj.CreateMaze(loadMaze='maze.csv')

    search_path, backtrack_path, solution_path = astar_solver(maze_obj)
    display_results(maze_obj, search_path, backtrack_path, solution_path)

    maze_obj.run()


if __name__ == '__main__':
    main()
