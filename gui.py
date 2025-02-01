import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from threading import Thread
import time
from model import IsingModel

# Create an instance of the IsingModel with default parameters
model = IsingModel(N=20, J=1.0, h=0.0, T=2.5, steps=100000)

def update_plot():
    """Update the visualization by running the metropolis steps and redrawing the plot."""
    while model.running:
        model.metropolis_step()
        ax.clear()
        ax.imshow(model.lattice, cmap='gray')
        ax.set_title(f"Ising Model (T={model.T:.2f})")
        canvas.draw()
        time.sleep(0.1)

def start_simulation():
    """Start the simulation in a separate thread."""
    if not model.running:
        model.running = True
        Thread(target=update_plot, daemon=True).start()

def stop_simulation():
    """Stop the simulation."""
    model.stop_simulation()

def update_temperature(val):
    """Update the simulation temperature from the slider value."""
    model.update_temperature(val)

def update_grid_size(val):
    """Update the grid size and reinitialize the lattice."""
    model.update_grid_size(val)

# GUI Setup
root = tk.Tk()
root.title("Ising Model Simulation")

# Matplotlib figure
fig, ax = plt.subplots()
ax.imshow(model.lattice, cmap='gray')
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Control Panel
tk.Button(root, text="Start", command=start_simulation).pack()
tk.Button(root, text="Stop", command=stop_simulation).pack()
tk.Label(root, text="Temperature").pack()
tk.Scale(root, from_=0.1, to=5, resolution=0.1, orient=tk.HORIZONTAL, command=update_temperature).pack()
tk.Label(root, text="Grid Size").pack()
tk.Scale(root, from_=10, to=50, resolution=1, orient=tk.HORIZONTAL, command=update_grid_size).pack()

root.mainloop()