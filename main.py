import tkinter as tk  # Import tkinter
from tkinter import messagebox  # Import messagebox for alerts
import time  # Import time for visualization delay

import Backtracking
from Grid import Grid


class Main:
   def __init__(self):
      self.root = tk.Tk()
      self.root.title("Sudoku Solver")

      # Sudoku grid
      self.sudoku_grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
      ]

      self.grid = Grid(self.sudoku_grid)
      self.entries = []

      # Pass the visualization callback to Backtracking
      self.solver = Backtracking.Backtracking(
            self.grid, update_callback=self.update_gui
      )

      # Create GUI
      self.create_grid()
      self.create_solve_button()

   def create_grid(self):
      for r in range(9):
            row_entries = []
            for c in range(9):
               value = self.grid.get_value(r, c)
               entry = tk.Entry(
                  self.root, width=2, font=("Arial", 18), justify="center"
               )
               entry.grid(row=r, column=c, padx=5, pady=5)
               if value != 0:
                  entry.insert(0, str(value))
                  entry.config(state="disabled")
               row_entries.append(entry)
            self.entries.append(row_entries)

   def create_solve_button(self):
      solve_button = tk.Button(self.root, text="Solve", command=self.solve_sudoku)
      solve_button.grid(row=10, column=0, columnspan=9, pady=10)

   def update_grid(self):
      for r in range(9):
            for c in range(9):
               if self.entries[r][c].get().isdigit():
                  self.grid.set_value(r, c, int(self.entries[r][c].get()))
               else:
                  self.grid.set_value(r, c, 0)

   def update_gui(self, r, c, value):
      """Callback function to update the GUI."""
      self.entries[r][c].delete(0, tk.END)
      if value != 0:
            self.entries[r][c].insert(0, str(value))
      self.root.update()  # Force GUI update

   def solve_sudoku(self):
      self.update_grid()
      if self.solver.solve():
            messagebox.showinfo("Success", "Sudoku solved!")
      else:
            messagebox.showerror("Error", "No solution exists!")

   def run(self):
      self.root.mainloop()


if __name__ == "__main__":
   app = Main()
   app.run()
