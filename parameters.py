"""
Model and simulation parameters for the stochastic market panic simulation.
All numerical values are defined here to separate the mathematical model
from experimental configurations.
"""

# -----------------------------
# Time discretization parameters
# -----------------------------

TOTAL_TIME = 15.0
DT = 0.01
NUM_STEPS = int(TOTAL_TIME / DT)

# -----------------------------
# Monte Carlo parameters
# -----------------------------

NUM_SIMULATIONS = 200

# -----------------------------
# Initial market conditions
# -----------------------------

INITIAL_PRICE = 100.0

# -----------------------------
# Normal market parameters
# -----------------------------

MU_NORMAL = 0.05
SIGMA_NORMAL = 0.2

# -----------------------------
# Panic event parameters
# -----------------------------

PANIC_TIME = 10.0
MU_PANIC = -0.15
SIGMA_PANIC = 0.6
