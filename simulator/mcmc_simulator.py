import numpy as np

class MCMCSimulator:
    def __init__(self, T=2.5, steps=1000):
        self.T = T
        self.steps = steps
        self.running = False

    def metropolis_step(self, model):
        """ Perform Metropolis-Hastings step """
        for _ in range(self.steps):
            i, j = np.random.randint(0, model.N, size=2)
            S = model.lattice[i, j]
            neighbors = model.lattice[(i+1) % model.N, j] + model.lattice[i, (j+1) % model.N] + \
                        model.lattice[(i-1) % model.N, j] + model.lattice[i, (j-1) % model.N]
            dE = 2 * model.J * S * neighbors + 2 * model.h * S
            if dE < 0 or np.random.rand() < np.exp(-dE / self.T):
                model.lattice[i, j] *= -1
    
    def run_simulation(self, model, callback=None):
        """ Run the simulation loop """
        self.running = True
        while self.running:
            self.__metropolis_step(model)

            if callback:
                callback()
            
            time.sleep(0.1)
    
    def stop_simulation(self):
        self.running = False