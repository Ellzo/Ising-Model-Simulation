# Add the project root to the system path
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Setup arguments
from argparse import ArgumentParser
parser = ArgumentParser("Perform a MCMC simulation of the Ising Model")
parser.add_argument("--temperature", type=float, default=1.0, help="Temperature used in Ising Model simulation")
parser.add_argument("--steps", type=int, default=1500, help="Number of steps in MCMC simulation")


from simulator import MCMCSimulator
from ising_model import IsingModel

import matplotlib.pyplot as plt

args = parser.parse_args()
T = args.temperature
steps = args.steps

model = IsingModel()
simulator = MCMCSimulator(T=T, steps=steps)
simulator.run_simulation(model, simulator.stop_simulation)

plt.imshow(model.lattice, cmap='gray')
plt.title(f"Ising Model at T={T} after {steps} steps")
plt.show()