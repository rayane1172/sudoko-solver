import tkinter as tk  # Import tkinter
from tkinter import messagebox  # Import messagebox for alerts
import Backtracking
from Grid import Grid


class Main:
   def __init__(self):
      self.root = tk.Tk()
      self.root.title("Sudoku Solver")

      # Create a blank Sudoku grid
      self.sudoku_grid = [[0 for _ in range(9)] for _ in range(9)]

      self.grid = Grid(self.sudoku_grid)
      self.entries = []

      # Pass the visualization callback to Backtracking
      self.solver = Backtracking.Backtracking(self.grid, update_callback=self.update_gui)

      self.create_grid()
      self.create_solve_button()

   def create_grid(self):
      for r in range(9):
            row_entries = []
            for c in range(9):
               entry = tk.Entry(self.root, width=2, font=("Arial", 18), justify="center")
               entry.grid(row=r, column=c, padx=5, pady=5)
               row_entries.append(entry)
            self.entries.append(row_entries)

   def create_solve_button(self):
      solve_button = tk.Button(self.root, text="Solve", command=self.solve_sudoku)
      solve_button.grid(row=10, column=0, columnspan=9, pady=10)

   def update_grid(self):
      # Retrieve values from GUI and update the grid object.
      for r in range(9):
            for c in range(9):
               value = self.entries[r][c].get()
               if value.isdigit():
                  self.grid.set_value(r, c, int(value))
               else:
                  self.grid.set_value(r, c, 0)

   def update_gui(self, r, c, value):
      self.entries[r][c].delete(0, tk.END)
      if value != 0:
            self.entries[r][c].insert(0, str(value))
      self.root.update()

   def solve_sudoku(self):
      self.update_grid()  # Fetch user input and update grid
      # todo -> to test every value in initial grid
      for row in range(9):
         for col in range(9):
            value = self.grid.get_value(row, col)
            if value != 0:
               # delete it to not reply it
               self.grid.set_value(row, col, 0)
               if not self.solver.is_valid(row, col, value):
                     # restore the value and show the error
                     self.grid.set_value(row, col, value)
                     messagebox.showerror("Invalid Input",f"Erreur : La valeur {value} à la position ({row+1}, {col+1}) est invalide.",)
                     return # to stop
               self.grid.set_value(row, col, value) # restore the value

      if self.solver.solve():
            messagebox.showinfo("Success", "Sudoku solved!")
      else:
            messagebox.showerror("Error", "No solution exists!")

   def run(self):
      self.root.mainloop()


if __name__ == "__main__":
   app = Main()
   app.run()
