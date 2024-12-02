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
      elif c == 9: # next row
            return self.solve(r + 1, 0)
      elif self.grid.get_value(r, c) != 0:  # skip existed value
            return self.solve(r, c + 1)
      else:
            for k in range(1, 10):
                  if self.is_valid(r, c, k):
                        self.grid.set_value(r, c, k)
                        if self.update_callback:
                              self.update_callback(r, c, k)  # call to update gui
                              time.sleep(0.02)
                        if self.solve(r, c + 1):  # next cell
                              return True
                        self.grid.set_value(r, c, 0)  # Backtrack using the setter
                        if self.update_callback:
                              self.update_callback(r, c, 0)  # call to update gui
                        time.sleep(0.02)
            return False
