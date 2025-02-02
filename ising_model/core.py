import numpy as np
import time

class IsingModel:
    def __init__(self, N=20, J=1.0, h=0.0, lattice=None):
        self.reintialize_model(N, J, h, lattice)
    
    def __energy(self):
        """ Compute total energy """
        E = 0
        for i in range(self.N):
            for j in range(self.N):
                S = self.lattice[i, j]
                neighbors = self.lattice[(i+1) % self.N, j] + self.lattice[i, (j+1) % self.N] + \
                            self.lattice[(i-1) % self.N, j] + self.lattice[i, (j-1) % self.N]
                E += -self.J * S * neighbors - self.h * S
        return E / 2
    
    def reintialize_model(self, N, J=None, h=None, lattice=None):
        if N:
            self.N = int(N)
        
        if J is not None:
            self.J = float(J)
        
        if h is not None:
            self.h = float(h)

        if not lattice:
            self.lattice = np.random.choice([-1, 1], size=(self.N, self.N))
        else:
            self.lattice = lattice
        
        self.energy = self.__energy()