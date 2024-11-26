import time


class Backtracking:
   def __init__(self, grid, update_callback=None):
      self.grid = grid  # Store the Grid instance
      self.update_callback = update_callback  # Callback for GUI updates

   def is_valid(self, r, c, k):
      not_in_row = k not in [self.grid.get_value(r, i) for i in range(9)]
      not_in_column = k not in [self.grid.get_value(i, c) for i in range(9)]
      not_in_box = k not in [
            self.grid.get_value(i, j)
            for i in range(r // 3 * 3, r // 3 * 3 + 3)
            for j in range(c // 3 * 3, c // 3 * 3 + 3)
      ]
      return not_in_row and not_in_column and not_in_box

   def solve(self, r=0, c=0):
      if r == 9:
            return True
      elif c == 9:  # Move to the next row
            return self.solve(r + 1, 0)
      elif self.grid.get_value(r, c) != 0:  # Skip already filled cells
            return self.solve(r, c + 1)
      else:
            for k in range(1, 10):  # Try numbers 1 through 9
                  if self.is_valid(r, c, k):
                        self.grid.set_value(r, c, k)  # Use setter to set the value
                        if self.update_callback:
                              self.update_callback(r, c, k)  # Trigger GUI update
                              time.sleep(0.02)  # Add a delay for visualization
                        if self.solve(r, c + 1):  # Recurse to the next cell
                              return True
                        self.grid.set_value(r, c, 0)  # Backtrack using the setter
                        if self.update_callback:
                              self.update_callback(r, c, 0)  # Trigger GUI update for backtracking
                        time.sleep(0.02)
            return False
