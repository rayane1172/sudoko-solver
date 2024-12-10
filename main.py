import tkinter as tk
from tkinter import messagebox
from Backtracking import Backtracking
from Grid import Grid
import sys

class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sudoku Solver TIAI")

        # todo -> create empty grid
        self.sudoku_grid = [[0 for _ in range(9)] for _ in range(9)]

        self.grid = Grid(self.sudoku_grid)
        self.entries = [] # grid in gui interface


        self.solver = Backtracking(self.grid, update_callback=self.update_gui)
        # todo -> update callback to notifiy the gui to update
        self.root.protocol("WM_DELETE_WINDOW", self.on_close) # close function

        self.create_grid()
        self.create_solve_button()

    def create_grid(self): #todo -> create grid in gui
        for r in range(9):
            row_entries = []
            for c in range(9):
                entry = tk.Entry(self.root, width=2, font=("Arial", 18), justify="center")
                entry.grid(row=r, column=c, padx=5, pady=5)
                row_entries.append(entry)
            self.entries.append(row_entries)

    def on_close(self):
        # Optional: Show a confirmation dialog
        if tk.messagebox.askyesno("Quit", "Are you sure you want to quit?"):
            self.root.destroy()  # Close the Tkinter window
            sys.exit()  # Exit the program

    def create_solve_button(self):
        solve_button = tk.Button(self.root, text="Solve", command=self.solve_sudoku)
        solve_button.grid(row=10, column=0, columnspan=9, pady=10)

    def update_grid(self): # todo -> get values from interface to grid object
        for r in range(9):
            for c in range(9):
                value = self.entries[r][c].get()
                if value.isdigit():
                    self.grid.set_value(r, c, int(value))
                else:
                    self.grid.set_value(r, c, 0)

    def update_gui(self, r, c, value): #todo-> update gui when call-back function called
        self.entries[r][c].delete(0, tk.END)
        if value != 0:
            self.entries[r][c].insert(0, str(value))
        self.root.update()

    def solve_sudoku(self): #todo -> to test if the initial grid is correct
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
