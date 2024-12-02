from pyMaze import maze,agent,COLOR, textLabel

def breadth_first_search(maze_instance):
    start_point = (maze_instance.rows, maze_instance.cols)
    visited_cells = [start_point]
    frontier_stack = [start_point]

    path_to_goal = {}
    search_order = []

    while len(frontier_stack) > 0:
        current_cell = frontier_stack.pop(0)
        search_order.append(current_cell)

        if current_cell == (1, 1):
            break

        for direction in "ESNW":
            if maze_instance.maze_map[current_cell][direction]==True:
                if direction == 'E':
                    neighbor = (current_cell[0], current_cell[1] + 1)
                elif direction == 'W':
                    neighbor = (current_cell[0], current_cell[1] - 1)
                elif direction == 'S':
                    neighbor = (current_cell[0] + 1, current_cell[1])
                elif direction == 'N':
                    neighbor = (current_cell[0] - 1, current_cell[1])

                if neighbor in visited_cells:
                    continue

                visited_cells.append(neighbor)
                frontier_stack.append(neighbor)
                path_to_goal[neighbor] = current_cell

    shortest_path = {}
    current_position = (1, 1)
    while current_position != start_point:
        shortest_path[path_to_goal[current_position]] = current_position
        current_position = path_to_goal[current_position]

    return search_order, shortest_path

def main():
    maze_instance = maze(10, 10)
    maze_instance.CreateMaze(loadMaze="maze.csv")

    explored_order, solution_path = breadth_first_search(maze_instance)

    explorer_agent = agent(maze_instance, footprints=True, shape='square', color=COLOR.green)
    maze_instance.tracePath({explorer_agent: explored_order}, showMarked=True)
    solver_agent = agent(maze_instance, footprints=True, color=COLOR.yellow)
    maze_instance.tracePath({solver_agent: solution_path})

    textLabel(maze_instance, 'BFS Path Length', len(solution_path) + 1)
    textLabel(maze_instance, 'BFS Search Length', len(explored_order))
    maze_instance.run()


if __name__ == "__main__":
    main()