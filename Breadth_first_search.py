from pyMaze import maze,agent,COLOR, textLabel
import time

def breadth_first_search(maze_obj):
    start_point = (maze_obj.rows, maze_obj.cols)
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
            if maze_obj.maze_map[current_cell][direction]==True:
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
    maze_obj = maze(100, 100) #Modify the maze size. Ex: maze(5, 5)
    #There is a maze.csv which I save for sumilation. To load the default maze use this line
    maze_obj.CreateMaze(loadMaze='maze-100-50.csv') 
    #change the loopPercent value to increase or decrease the cells obstacles number
    # maze_obj.CreateMaze(loopPercent=50, saveMaze=True) 

    start_time = time.time()
    explored_order, solution_path = breadth_first_search(maze_obj)
    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time  # Calculate execution time

    explorer_agent = agent(maze_obj, footprints=True, shape='square', color=COLOR.green)
    maze_obj.tracePath({explorer_agent: explored_order}, showMarked=True, delay=100)
    solver_agent = agent(maze_obj, footprints=True, color=COLOR.yellow)
    maze_obj.tracePath({solver_agent: solution_path}, delay=100)

    textLabel(maze_obj, 'BFS Path Length', len(solution_path) + 1)
    textLabel(maze_obj, 'BFS Search Length', len(explored_order))

    print('Breadth-First Search Path Length', len(solution_path) + 1)
    print('Breadth-First Search Length', len(explored_order))
    print("Execution Time: ", execution_time)
    maze_obj.run()


if __name__ == "__main__":
    main()