import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from simulator import MCMCSimulator
from tkinter import ttk
from threading import Thread


class GUISimulator:
    def __init__(self, model, T=2.5, steps=1000):
        self.simulator = MCMCSimulator(T=T, steps=steps)
        self.model = model
    
    def create_gui(self):
        # GUI Setup
        root = tk.Tk()
        root.title("Ising Model Simulation")
        root.configure(bg="#f0f0f0")

        # Matplotlib figure
        fig, self.ax = plt.subplots()
        self.ax.imshow(self.model.lattice, cmap='seismic', vmin=-1, vmax=1)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.canvas = FigureCanvasTkAgg(fig, master=root)
        self.canvas.get_tk_widget().pack(pady=10)

        # Control Panel
        frame = ttk.Frame(root, padding=10)
        frame.pack()

        ttk.Button(frame, text="Start", command=self.run_simulation).pack(pady=5)
        ttk.Button(frame, text="Stop", command=self.stop_simulation).pack(pady=5)

        ttk.Label(frame, text="Temperature", font=("Arial", 12, "bold")).pack()
        temperature_slider = ttk.Scale(frame, from_=0.1, to=5, orient=tk.HORIZONTAL, command=self.set_temperature)
        temperature_slider.set(self.simulator.T)
        temperature_slider.pack(pady=5)

        ttk.Label(frame, text="Grid Size", font=("Arial", 12, "bold")).pack()
        grid_slider = ttk.Scale(frame, from_=10, to=50, orient=tk.HORIZONTAL, command=self.update_grid_size)
        grid_slider.pack(pady=5)

        root.mainloop()
    
    def update_plot(self):
        self.ax.clear()
        self.ax.imshow(self.model.lattice, cmap='seismic', vmin=-1, vmax=1)
        self.ax.set_title(f"Ising Model (T={self.simulator.T:.2f})", fontsize=14, fontweight='bold')
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.grid(color='gray', linestyle='--', linewidth=0.5)
        self.canvas.draw()
    
    def run_simulation(self):
        Thread(target=lambda: self.simulator.run_simulation(self.model, callback=self.update_plot), daemon=True).start()
    
    def stop_simulation(self):
        self.simulator.stop_simulation()
    
    def set_temperature(self, T):
        self.simulator.T = float(T)
        self.update_plot()
    
    def update_grid_size(self, N):
        self.simulator.stop_simulation()
        self.model.reintialize_model(N)
        self.update_plot()
    
    