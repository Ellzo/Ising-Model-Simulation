# Add the project root to the system path
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from gui import GUISimulator
from ising_model import IsingModel

import matplotlib.pyplot as plt

model = IsingModel()
simulator = GUISimulator(model)
simulator.create_gui()