import tkinter as tk

# Create window and make it full screen

win = tk.Tk()
win.after(10, lambda: win.state("zoomed"))

# Create frames and arrange into a grid.

win.grid_rowconfigure(0, weight=1)
win.grid_rowconfigure(1, weight=1)
win.grid_columnconfigure(0, weight=1)
win.grid_columnconfigure(1, weight=1)

f1 = tk.Frame(win, bg="#3F3F3F")
f1.grid(row=0, column=0, rowspan=2, padx=20, pady=20, sticky="nsew")

f2 = tk.Frame(win, bg="#3F3F3F")
f2.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

f3 = tk.Frame(win, bg="#3F3F3F")
f3.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

win.mainloop()