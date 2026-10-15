"""Hello-world test window for the letter tracker.

Purpose: check that the GitHub build works on Linux, Windows and macOS.
It also tries the two things the real app will need: a ttk widget
and the clipboard.
"""
import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    """The main window. Inheriting from tk.Tk means App *is* a window."""

    def __init__(self):
        super().__init__()  # set up the underlying tkinter window first
        self.title("Letter Tracker - test")
        self.geometry("360x200")

        # State that belongs to the window lives on "self".
        self.clicks = 0

        self.label = ttk.Label(self, text="Hello! The build works.")
        self.label.pack(pady=(20, 10))

        self.button = ttk.Button(self, text="Click me", command=self.on_click)
        self.button.pack(pady=5)

        self.copy_button = ttk.Button(
            self, text="Copy text to clipboard", command=self.copy_text
        )
        self.copy_button.pack(pady=5)

        self.combo = ttk.Combobox(self, values=["Anna", "Ben", "Clara"])
        self.combo.pack(pady=5)

    # Methods are functions that belong to the class. "self" gives them
    # access to the window's widgets and state.
    def on_click(self):
        self.clicks += 1
        self.label.config(text=f"Clicked {self.clicks} time(s)")

    def copy_text(self):
        self.clipboard_clear()
        self.clipboard_append("Clipboard test: it works!")
        self.label.config(text="Copied - paste it somewhere to check")


if __name__ == "__main__":
    App().mainloop()
