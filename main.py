import tkinter as tk
from tkinter import ttk

# Will be using Tkinter instead of CustomTkinter, otherwise every user would have to install CustomTkinter separately.
# The theme is nice though, so we will use that.

# Apply the theme to the window.
def apply_ctk_clam_theme(root):
    
    # Colour palette from CustomTkinter
    DARK_BG = "#2b2b2b"
    DARK_FG = "#eeeeee"
    ENTRY_BG = "#3c3c3c"
    ACCENT = "#1f6aa5"
    ACCENT_HOVER = "#144870"

    # Grab and modify universal style
    style = ttk.Style(root)
    style.theme_use("clam")
    root.configure(bg=DARK_BG)
    style.configure(".",
                font=("Segoe UI", 11),
                foreground="#eeeeee",
                background="#2b2b2b",
                focuscolor=ACCENT)
    
    # --------------- SPECIAL CASES - Need their own specific configurations.

    # Entry box
    style.configure("TEntry",
                    fieldbackground=ENTRY_BG,
                    foreground="DARK_FG",
                    insertcolor=DARK_FG,
                    padding=5)

    # Dropdown menu
    style.configure("TCombobox",
                    fieldbackground=ENTRY_BG,
                    background=ENTRY_BG,
                    foreground=DARK_FG,
                    arrowcolor="white",
                    padding=5)
    
    # Style map for hovering on the checkbutton
    style.map("TCheckbutton",
              foreground=[("active", DARK_FG)],
              background=[("active", DARK_BG)])
    
    # Making the button blue
    style.configure("TButton",
                background=ACCENT,   # idle/default color
                foreground="white",
                relief="flat")
    # Hovering on the button
    style.map("TButton",
              background=[("active", ACCENT_HOVER)],
              foreground=[("disabled", "#aaaaaa")])



# --- Demo app ---
if __name__ == "__main__":
    
    root = tk.Tk()
    root.title("CTk-like Clam Theme")
    apply_ctk_clam_theme(root)

    frame = ttk.Frame(root, padding=20)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="This is a CTk-like clam theme").pack(pady=10)
    ttk.Entry(frame).pack(pady=10)
    ttk.Button(frame, text="Click Me").pack(pady=10)
    ttk.Checkbutton(frame, text="Check me").pack(pady=10)
    ttk.Combobox(frame, values=["Option 1", "Option 2", "Option 3"]).pack(pady=10)

    root.mainloop()
