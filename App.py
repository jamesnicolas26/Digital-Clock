import tkinter as tk
import time

def update_clock():
    """Update the clock every second."""
    current_time = time.strftime("%H:%M:%S")
    label_clock.config(text=current_time)
    label_clock.after(1000, update_clock)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Create and place widgets
label_clock = tk.Label(root, font=("Arial", 48), bg="black", fg="white")
label_clock.pack(expand=True, fill=tk.BOTH)

# Start the clock update loop
update_clock()

# Start the main loop
root.mainloop()
