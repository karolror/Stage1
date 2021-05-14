import tuner
import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x500")
    root.maxsize(800, 500)
    root.minsize(800, 500)
    root.title("Stage1 Generator")
    tuner.Tuner(root)
    root.mainloop()
