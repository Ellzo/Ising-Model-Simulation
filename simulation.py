import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 20  # Lattice size (N x N)
J = 1.0  # Interaction strength
h = 0.0  # External magnetic field
T = 2.5  # Temperature
steps = 100000  # Number of iterations

# Initialize lattice randomly with +1 or -1 spins
lattice = np.random.choice([-1, 1], size=(N, N))

def energy(lattice):
    """ Compute the total energy of the system """
    E = 0
    for i in range(N):
        for j in range(N):
            S = lattice[i, j]
            neighbors = lattice[(i+1) % N, j] + lattice[i, (j+1) % N] + \
                        lattice[(i-1) % N, j] + lattice[i, (j-1) % N]
            E += -J * S * neighbors - h * S
    return E / 2  # Each pair counted twice

def metropolis_step(lattice, T):
    """ Perform one Metropolis-Hastings step """
    i, j = np.random.randint(0, N, size=2)  # Pick a random spin
    S = lattice[i, j]
    
    # Compute energy change if we flip the spin
    neighbors = lattice[(i+1) % N, j] + lattice[i, (j+1) % N] + \
                lattice[(i-1) % N, j] + lattice[i, (j-1) % N]
    
    dE = 2 * J * S * neighbors + 2 * h * S  # Energy difference
    
    # Accept or reject the move
    if dE < 0 or np.random.rand() < np.exp(-dE / T):
        lattice[i, j] *= -1  # Flip spin

# Run MCMC Simulation
for step in range(steps):
    metropolis_step(lattice, T)

# Plot final configuration
plt.imshow(lattice, cmap='gray')
plt.title(f"Ising Model at T={T}")
plt.show()
