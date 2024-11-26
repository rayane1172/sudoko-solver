class Grid:
   def __init__(self, grid):
      self.grid = grid

   def get_value(self, row, col):
      return self.grid[row][col]

   def set_value(self, row, col, value):
      self.grid[row][col] = value

   def is_empty(self, row, col):
      return self.grid[row][col] == 0

   def display(self):
      for row in self.grid:
            print(" ".join(str(num) if num != 0 else "." for num in row))  # Show "." in empty places

   def get_grid(self):
      return self.grid
