import numpy as np
import time

class IsingModel:
    def __init__(self, N=20, J=1.0, h=0.0, T=2.5, steps=1000):
        self.N = N  # Grid size
        self.J = J  # Interaction strength
        self.h = h  # External field
        self.T = T  # Temperature
        self.steps = steps  # Steps per update
        self.lattice = np.random.choice([-1, 1], size=(N, N))
        self.running = False
    
    def energy(self):
        """ Compute total energy """
        E = 0
        for i in range(self.N):
            for j in range(self.N):
                S = self.lattice[i, j]
                neighbors = self.lattice[(i+1) % self.N, j] + self.lattice[i, (j+1) % self.N] + \
                            self.lattice[(i-1) % self.N, j] + self.lattice[i, (j-1) % self.N]
                E += -self.J * S * neighbors - self.h * S
        return E / 2
    
    def metropolis_step(self):
        """ Perform Metropolis-Hastings step """
        for _ in range(self.steps):
            i, j = np.random.randint(0, self.N, size=2)
            S = self.lattice[i, j]
            neighbors = self.lattice[(i+1) % self.N, j] + self.lattice[i, (j+1) % self.N] + \
                        self.lattice[(i-1) % self.N, j] + self.lattice[i, (j-1) % self.N]
            dE = 2 * self.J * S * neighbors + 2 * self.h * S
            if dE < 0 or np.random.rand() < np.exp(-dE / self.T):
                self.lattice[i, j] *= -1
    
    def update_temperature(self, T):
        self.T = float(T)
    
    def update_grid_size(self, N):
        self.N = int(N)
        self.lattice = np.random.choice([-1, 1], size=(self.N, self.N))
    
    def run_simulation(self, callback):
        """ Run the simulation loop """
        self.running = True
        while self.running:
            self.metropolis_step()
            callback()
            time.sleep(0.1)
    
    def stop_simulation(self):
        self.running = False
