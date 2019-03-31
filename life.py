
class Life:

    def __init__(self, x_dim, y_dim):
        self.__grid_x_dim = x_dim
        self.__grid_y_dim = y_dim
        self.__grid = ["-" for j in range(x_dim * y_dim)]

    def get_grid(self):
        return self.__grid

    def get_grid_dim(self):
        return self.__grid_x_dim, self.__grid_y_dim

    def process_life(self):
        cell_changes = self.get_iteration_cell_changes()

        for change in cell_changes:
            self.__grid[change[0]] = "*" if change[1] else "-"

    def get_iteration_cell_changes(self):
        cell_changes = []
        for cell_no in range(len(self.__grid)):

            populated = self.__grid[cell_no] == "*"
            will_live = False
            change = False
            neighbour_count = self.get_neighbour_count(cell_no)

            # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
            # Any live cell with two or three live neighbours lives on to the next generation.
            # Any live cell with more than three live neighbours dies, as if by overpopulation.
            # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
            if neighbour_count < 2 and populated:
                change = True
                will_live = False
            if neighbour_count >= 2 and populated:
                change = False
            if neighbour_count == 3 and not populated:
                change = True
                will_live = True
            if neighbour_count > 3 and populated:
                change = True
                will_live = False

            if change:
                cell_changes.append([cell_no, will_live])

        return cell_changes

    def get_neighbour_count(self, cell_no):
        neighbour_count = 0
        adj_cells = self.get_adjacent_cells(cell_no)
        for cell in adj_cells:
            if cell < 0 or cell > len(self.__grid) - 1 or cell == cell_no:
                continue
            if self.__grid[cell] == "*":
                neighbour_count += 1

        return neighbour_count

    def get_adjacent_cells(self, cell_no):
        return [cell_no - self.__grid_x_dim - 1, cell_no - self.__grid_x_dim, cell_no - self.__grid_x_dim + 1,
                cell_no - 1, cell_no, cell_no + 1,
                cell_no + self.__grid_x_dim - 1, cell_no + self.__grid_x_dim, cell_no + self.__grid_x_dim + 1]

    def get_population(self):
        return self.__grid.count("*")

    def set_cell(self, cell_no, on_off):
        self.__grid[cell_no] = "*" if on_off else "-"
